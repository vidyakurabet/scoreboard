import random, statistics
from scoreboard import Scoreboard

def check(stream):
    sb = Scoreboard()
    for i, x in enumerate(stream):
        got = sb.add(x)
        want = statistics.median(stream[:i + 1])
        assert got == want, (stream[:i + 1], got, want)

check([5])
check([7] * 10)
check([-5, -1, -9, -3])
check([5, 1, 9, 3])
check([-2147483648, 2147483647, 0, 2147483647, -2147483648])

for _ in range(200):
    check([random.randint(-50, 50) for _ in range(random.randint(1, 60))])

print("All tests passed")
