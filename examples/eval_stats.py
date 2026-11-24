import math


def bernoulli_se(p, n):
    """Standard error of an accuracy p estimated on n independent questions."""
    return math.sqrt(p * (1 - p) / n)


def unpaired_z(acc_a, acc_b, n):
    """z-score of the gap between two accuracies measured on separate samples of n questions."""
    se = math.sqrt(bernoulli_se(acc_a, n) ** 2 + bernoulli_se(acc_b, n) ** 2)
    return (acc_a - acc_b) / se


def paired_z(a, b):
    """(difference, standard error, z) when both models answered the SAME questions.
    a and b hold each model's 0/1 score, in the same question order."""
    n = len(a)
    d = [x - y for x, y in zip(a, b)]  # +1, 0 or -1 for each question
    diff = sum(d) / n
    se = math.sqrt(sum((x - diff) ** 2 for x in d) / (n - 1) / n)
    return diff, se, diff / se


for n in (100, 1000, 10000):
    print(f"n={n:>5}  SE = {bernoulli_se(0.70, n):.4f}")

print(f"unpaired: z = {unpaired_z(0.75, 0.64, 100):.2f}")

# 60 questions: both right. 15: only A right. 4: only B right. 21: both wrong.
pairs = [(1, 1)] * 60 + [(1, 0)] * 15 + [(0, 1)] * 4 + [(0, 0)] * 21
diff, se, z = paired_z(*zip(*pairs))
print(f"paired:   difference = {diff:.2f}, SE = {se:.4f}, z = {z:.2f}")
