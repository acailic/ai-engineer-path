/* AI Engineer Path site: theme, course menu, reading progress, and reading a page aloud with the browser's own voices. */
(function () {
  "use strict";
  var root = document.documentElement;
  function store(key, value) {
    try {
      if (value === undefined) return localStorage.getItem(key);
      localStorage.setItem(key, value);
    } catch (e) { return null; }
  }

  /* ---- theme and course menu ---- */
  var themeBtn = document.getElementById("theme-toggle");
  if (themeBtn) themeBtn.addEventListener("click", function () {
    var dark = root.dataset.theme ? root.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
    root.dataset.theme = dark ? "light" : "dark";
    store("aep-theme", root.dataset.theme);
  });
  var menuBtn = document.getElementById("menu-toggle"), overlay = document.getElementById("overlay");
  function menu(open) {
    document.body.classList.toggle("nav-open", open);
    menuBtn.setAttribute("aria-expanded", String(open));
    menuBtn.setAttribute("aria-label", open ? "Close the course menu" : "Open the course menu");
    overlay.hidden = !open;
  }
  if (menuBtn) {
    menuBtn.addEventListener("click", function () { menu(!document.body.classList.contains("nav-open")); });
    overlay.addEventListener("click", function () { menu(false); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") menu(false); });
  }

  /* ---- reading progress ---- */
  var bar = document.getElementById("progress-bar");
  function progress() {
    var height = root.scrollHeight - innerHeight;
    bar.style.width = (height > 0 ? Math.min(100, 100 * scrollY / height) : 100) + "%";
  }
  addEventListener("scroll", progress, { passive: true });
  addEventListener("load", progress);
  progress();

  var toc = document.querySelector(".toc");
  if (toc && !toc.querySelector("a")) toc.remove();

  /* ---- read aloud ---- */
  var main = document.getElementById("content"), box = document.getElementById("listen");
  var supported = main && box && "speechSynthesis" in window && typeof SpeechSynthesisUtterance === "function";
  if (!supported) { if (box) box.hidden = true; return; }
  var synth = window.speechSynthesis;
  function $(id) { return document.getElementById(id); }
  var playBtn = $("listen-play"), panel = $("listen-panel"), status = $("listen-status");
  var rateSel = $("listen-rate"), voiceSel = $("listen-voice"), follow = $("listen-follow");
  var SEL = "h1, h2, h3, h4, p, li, blockquote, summary, tr, dt, dd";
  var blocks = [], byEl = new Map(), index = 0, active = false, token = 0, voices = [];

  // Symbols that a voice reads badly are spelled out.
  function clean(s) {
    return s.replace(/→/g, ", leads to,").replace(/·/g, ",").replace(/—/g, ",")
            .replace(/(\d)\s*[–-]\s*(\d)/g, "$1 to $2").replace(/≤/g, " at most ").replace(/≥/g, " at least ")
            .replace(/×/g, " times ").replace(/≠/g, " is not equal to ").replace(/~/g, " about ")
            .replace(/\s+/g, " ").trim();
  }
  // The words of one block itself: nested lists, code, diagrams and buttons are left out.
  function ownText(el) {
    var copy = el.cloneNode(true);
    copy.querySelectorAll("ul, ol, pre, code, svg, script, .anchor, .play-from").forEach(function (n) { n.remove(); });
    return clean(copy.textContent);
  }
  function collect() {
    main.querySelectorAll(SEL).forEach(function (el) {
      if (el.closest("pre, .mermaid, svg, nav.pager")) return;
      var tag = el.tagName;
      // Text inside a list item, a quotation or a table row is read once, with its parent.
      if (tag !== "LI" && el.parentElement.closest("li")) return;
      if (tag !== "BLOCKQUOTE" && el.parentElement.closest("blockquote")) return;
      if (tag !== "TR" && el.parentElement.closest("tr")) return;
      var text = ownText(el);
      if (!text) return;
      byEl.set(el, blocks.length);
      blocks.push({ el: el, text: text });
    });
  }
  // Sentences are grouped into short pieces: some browsers cut a long utterance off.
  function pieces(sentence) {
    var line = "", out = [];
    sentence.split(" ").forEach(function (w) {
      if ((line + " " + w).length > 180 && line) { out.push(line); line = w; } else line = line ? line + " " + w : w;
    });
    if (line) out.push(line);
    return out;
  }
  function chunks(text) {
    var sentences = text.match(/[^.!?]+[.!?]+["')\]]*\s*|[^.!?]+$/g) || [text], out = [], current = "";
    sentences.forEach(function (s) {
      if (s.length > 180) {
        if (current) { out.push(current); current = ""; }
        pieces(s).forEach(function (p) { out.push(p); });
      } else if ((current + s).length > 180) { out.push(current); current = s; } else current += s;
    });
    if (current.trim()) out.push(current);
    return out.map(function (c) { return c.trim(); }).filter(Boolean);
  }
  function pick(list) {
    var names = ["Google US English", "Samantha", "Microsoft Aria", "Microsoft Jenny", "Google UK English Female", "Daniel", "Karen", "Microsoft Guy", "Microsoft Zira", "Alex", "Victoria"];
    for (var i = 0; i < names.length; i++) {
      var j = list.findIndex(function (v) { return v.name.indexOf(names[i]) >= 0; });
      if (j >= 0) return j;
    }
    var k = list.findIndex(function (v) { return /natural|neural|premium|enhanced/i.test(v.name); });
    return k >= 0 ? k : 0;
  }
  function loadVoices() {
    var all = synth.getVoices();
    voices = all.filter(function (v) { return /^en/i.test(v.lang); });
    if (!voices.length) voices = all;
    var saved = store("aep-voice");
    voiceSel.innerHTML = "";
    voices.forEach(function (v, i) {
      var option = document.createElement("option");
      option.value = String(i);
      option.textContent = v.name + " · " + v.lang;
      voiceSel.appendChild(option);
    });
    var chosen = saved ? voices.findIndex(function (v) { return v.name === saved; }) : -1;
    voiceSel.value = String(chosen >= 0 ? chosen : (voices.length ? pick(voices) : 0));
    voiceSel.parentElement.hidden = voices.length < 2;
  }
  function mark(i) {
    main.querySelectorAll(".speaking").forEach(function (n) { n.classList.remove("speaking"); });
    var block = blocks[i];
    if (!block) return;
    block.el.classList.add("speaking");
    status.textContent = "Reading " + (i + 1) + " of " + blocks.length;
    if (follow.checked) block.el.scrollIntoView({ block: "center", behavior: "smooth" });
  }
  function speak(i, my) {
    if (!active || my !== token) return;
    if (i < 0 || i >= blocks.length) return finish(true, my);
    index = i;
    mark(i);
    var parts = chunks(blocks[i].text), at = 0;
    function next() {
      if (!active || my !== token) return;
      if (at >= parts.length) return speak(i + 1, my);
      var utterance = new SpeechSynthesisUtterance(parts[at++]);
      utterance.rate = parseFloat(rateSel.value);
      var voice = voices[parseInt(voiceSel.value, 10)];
      if (voice) { utterance.voice = voice; utterance.lang = voice.lang; } else utterance.lang = "en-US";
      utterance.onend = next;
      utterance.onerror = next;
      synth.speak(utterance);
    }
    next();
  }
  function go(i, my) {
    if (my !== token) return;
    active = true;
    document.body.classList.add("reading");
    playBtn.textContent = "⏸ Pause";
    playBtn.setAttribute("aria-pressed", "true");
    panel.hidden = false;
    speak(i, my);
  }
  // The first utterance of a click is spoken at once: a phone browser only allows speech inside the click itself.
  function start(i) {
    var my = ++token;
    loadVoices();
    if (!synth.getVoices().length) {
      status.textContent = "This browser has no speech voices. Try Chrome, Edge or Safari.";
      panel.hidden = false;
      return;
    }
    if (synth.speaking || synth.pending) {
      synth.cancel();
      setTimeout(function () { go(i, my); }, 120);
    } else go(i, my);
  }
  function stop(done) {
    token++;
    synth.cancel();
    active = false;
    document.body.classList.remove("reading");
    main.querySelectorAll(".speaking").forEach(function (n) { n.classList.remove("speaking"); });
    playBtn.textContent = done ? "▶ Read again" : "▶ Resume";
    playBtn.setAttribute("aria-pressed", "false");
    if (done) { index = 0; status.textContent = "Finished this page."; }
    else status.textContent = "Paused at " + (index + 1) + " of " + blocks.length + ". Click Resume to hear this paragraph again.";
  }

  collect();
  rateSel.value = store("aep-rate") || "1";
  follow.checked = store("aep-follow") !== "0";
  loadVoices();
  if (synth.onvoiceschanged !== undefined) synth.onvoiceschanged = loadVoices;

  playBtn.addEventListener("click", function () { if (active) stop(false); else start(Math.min(index, blocks.length - 1)); });
  $("listen-stop").addEventListener("click", function () { stop(false); index = 0; status.textContent = "Stopped."; playBtn.textContent = "▶ Read aloud"; });
  $("listen-prev").addEventListener("click", function () { start(Math.max(0, index - 1)); });
  $("listen-next").addEventListener("click", function () { start(Math.min(blocks.length - 1, index + 1)); });
  rateSel.addEventListener("change", function () { store("aep-rate", rateSel.value); });
  voiceSel.addEventListener("change", function () { store("aep-voice", voices[parseInt(voiceSel.value, 10)].name); });
  follow.addEventListener("change", function () { store("aep-follow", follow.checked ? "1" : "0"); });

  // A small button on each heading starts the reading from there; a click on a paragraph jumps to it.
  main.querySelectorAll("h2, h3").forEach(function (heading) {
    if (!byEl.has(heading)) return;
    var button = document.createElement("button");
    button.className = "play-from";
    button.type = "button";
    button.textContent = "▶";
    button.setAttribute("aria-label", "Read from this heading");
    button.addEventListener("click", function (e) { e.preventDefault(); start(byEl.get(heading)); });
    heading.insertBefore(button, heading.firstChild);
  });
  main.addEventListener("click", function (e) {
    if (!active || e.target.closest("a, button, input, select, summary")) return;
    var block = e.target.closest(SEL), i = block ? byEl.get(block) : undefined;
    if (i !== undefined && i !== index) start(i);
  });
  // For checks in the browser console: window.__aep.blocks.length
  window.__aep = { blocks: blocks, get index() { return index; }, get active() { return active; } };
})();
