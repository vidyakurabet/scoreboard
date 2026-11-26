import random, time
from scoreboard import Scoreboard

def heap_time(data):
    sb = Scoreboard()
    t = time.perf_counter()
    for x in data:
        sb.add(x)
    return time.perf_counter() - t

def sort_time(data):
    seen = []
    t = time.perf_counter()
    for x in data:
        seen.append(x)
        s = sorted(seen)
        n = len(s)
        m = s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2
    return time.perf_counter() - t

print("n     heap(s)   sort(s)")
for n in [500, 1000, 2000, 4000]:
    data = [random.randint(-2*31, 2*31 - 1) for _ in range(n)]
    print(n, round(heap_time(data), 4), round(sort_time(data), 4))

big = [random.randint(-2*31, 2*31 - 1) for _ in range(100000)]
print("100000 scores, heap only:", round(heap_time(big), 3), "s")
