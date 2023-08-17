import matplotlib.pyplot as plt



n = 35

fact = [1 for _ in range(n + 1)]
val = 1
for i in range(1, n + 1):
    val *= i
    fact[i] = val

def choose(n, k):
    return fact[n] // (fact[n-k] * fact[k])

def central(n):
    return fact[2*n] // (fact[n] * fact[n])

x = range(n + 1)
y = [choose(n, j) for j in range(n + 1)]

fig, ax = plt.subplots()
ax.bar(x, y)
plt.show()