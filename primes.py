import math
import matplotlib.pyplot as plt


# vrne seznam prastevil manjsih od n
def eratosten(n):
    isPrime = [i >= 2 for i in range(n)]
    primes = []
    for i in range(2, n):
        if isPrime[i]:
            primes.append(i)
            for j in range(i*i, n, i):
                isPrime[j] = False
    return isPrime, primes

def Pi(isPrime):
    pi = []
    count = 0
    for i in range(len(isPrime)):
        if isPrime[i]:
            count += 1
        pi.append(count)
    return pi


        

n = 100
isPrime, primes = eratosten(n)
pi = Pi(isPrime)
x = range(2, n)
y1 = [pi[i] for i in x]
y2 = [i/math.log(i) for i in x]



fig, ax = plt.subplots()
ax.plot(x, y1, label="Pi")
ax.plot(x, y2, label="n/log(n)")
#ax.set_xlim(-5, 5)
#ax.set_ylim(0, 25)
plt.show()