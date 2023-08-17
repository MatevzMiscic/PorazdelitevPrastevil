import math
import matplotlib.pyplot as plt


n = 1000

val = 1
x = range(1, n + 1)
y1 = []
y2 = []

for i in range(1, n + 1):
    y1.append(i*math.log(4) - math.log(2*i))
    y2.append(math.sqrt(2*i) * math.log(2*i) + 2*i/3 * math.log(4))



fig, ax = plt.subplots()
ax.plot(x, y1, color="tab:blue")
ax.plot(x, y2, color="tab:orange")
plt.show()
