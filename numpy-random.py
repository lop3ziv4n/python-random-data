import numpy as np

print(np.random.random())

np.random.seed(123)
print(np.random.randint(1, 100))

nums = [5, 6, 7, 8, 9]
print(np.random.choice(nums))
# no .choices() and .sample() is different
print(np.random.sample(nums))

np.random.shuffle(nums)
print(nums)

# randint isn't inclusive of upper bounds
die_rolls1 = np.random.randint(1, 7, 100)
print(die_rolls1)

die_rolls2 = np.random.randint(1, 7, 100)
combo_rolls = zip(die_rolls1, die_rolls2)
combos = [a + b for a, b in combo_rolls]
print(combos)

import matplotlib.pyplot as plt

plt.hist(combos, 100)
plt.show()

print(np.random.normal(7, 1, 100))

print(np.random.randn(5, 3))


def corr2cov(p: np.ndarray, s: np.ndarray) -> np.ndarray:
    """Covariance matrix from correlation & standard deviation"""
    d = np.diag(s)
    return d @ p @ d


corr = np.array([[1, 0.9], [0.9, 1]])
stdev = np.array([14, 25])
mean = np.array([38, 10])
cov = corr2cov(corr, stdev)
print(cov)
data = np.random.multivariate_normal(mean=mean, cov=cov, size=500)
print(data[:10])

X, Y = zip(*data)
plt.scatter(X, Y)
