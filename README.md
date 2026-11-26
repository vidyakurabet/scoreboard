 # Live Score Statistics System

Maintains the running median of a stream of scores without re-sorting.

## How it works
- A max-heap holds the smaller half of the scores and a min-heap holds the larger half.
- The heap sizes differ by at most one, and every score in the lower half is less than or equal to every score in the upper half.
- The median is the top of the lower heap (odd count) or the mean of both tops (even count).
- Each insert costs O(log n). Sorting after every insert costs O(n log n).

## Files
- scoreboard.py: heap-based Scoreboard with history
- test_scoreboard.py: tests against statistics.median
- baseline.py: timing comparison against full sorting
- graphs.py: table and graphs (needs matplotlib)
- scores.txt: replay file, one score per line

## Run
python scoreboard.py
python test_scoreboard.py
python baseline.py
python graphs.py

## Results
Handles 100,000 scores in about 0.25 s. See graphs.png for heap vs sorting.
