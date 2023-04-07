# You are given an array A of size N. In one operation, you can do the following:
# Select indices i and j (i≠j) and set Ai = Aj.
# Find the minimum number of operations required to make all elements of the array equal.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    c = Counter(arr)
    ans = n-max(c.values())
    print(ans)
