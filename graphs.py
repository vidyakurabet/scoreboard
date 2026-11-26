import random, time
import matplotlib.pyplot as plt
from scoreboard import Scoreboard

# Part 1: table and graph of running medians
scores = [random.randint(-100, 100) for _ in range(40)]
scores += [-2147483648, 2147483647, 7, 7, 7]
sb = Scoreboard()
print("No.  Score  Median")
for i, s in enumerate(scores, 1):
    print(i, s, sb.add(s))

# Part 2: heap vs sorting timings
sizes = [500, 1000, 2000, 4000]
heap_t, sort_t = [], []
for n in sizes:
    data = [random.randint(-2*31, 2*31 - 1) for _ in range(n)]
    b = Scoreboard()
    t = time.perf_counter()
    for x in data:
        b.add(x)
    heap_t.append(time.perf_counter() - t)
    seen = []
    t = time.perf_counter()
    for x in data:
        seen.append(x)
        sorted(seen)
    sort_t.append(time.perf_counter() - t)

plt.figure(figsize=(11, 4))
plt.subplot(1, 2, 1)
plt.plot(sb.history)
plt.title("Running median")
plt.xlabel("Scores added")
plt.ylabel("Median")
plt.subplot(1, 2, 2)
plt.plot(sizes, heap_t, marker="o", label="Heap")
plt.plot(sizes, sort_t, marker="o", label="Sort every time")
plt.title("Time vs number of scores")
plt.xlabel("Scores (n)")
plt.ylabel("Seconds")
plt.legend()
plt.tight_layout()
plt.savefig("graphs.png")
plt.show()
