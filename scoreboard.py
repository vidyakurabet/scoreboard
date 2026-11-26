import heapq

class Scoreboard:
    def __init__(self):
        self.low = []    # max-heap (stored as negatives)
        self.high = []   # min-heap
        self.history = []

    def add(self, x):
        if not self.low or x <= -self.low[0]:
            heapq.heappush(self.low, -x)
        else:
            heapq.heappush(self.high, x)
        if len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))
        if len(self.low) > len(self.high):
            m = -self.low[0]
        else:
            m = (-self.low[0] + self.high[0]) / 2
        self.history.append(m)
        return m

    def count(self):
        return len(self.low) + len(self.high)

if __name__ == "__main__":
    sb = Scoreboard()
    with open("scores.txt") as f:
        for line in f:
            if line.strip():
                s = int(line)
                print(s, "->", sb.add(s))
    print("Count:", sb.count(), "Latest median:", sb.history[-1])
