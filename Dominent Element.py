# You are given an array A of length N. An element X is said to be dominant if the frequency of X in A is strictly greater than the frequency of any other element in the A.
# For example, if A=[2,1,4,4,4] then 4 is a dominant element since its frequency is higher than the frequency of any other element in A. Find if there exists any
# dominant element in A.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from collections import Counter
t = int(input())
while t>0:
    n = int(input())
    arr = list(map(int, input().split()))
    c = Counter(arr)
    valList = list(c.values())
    valList.sort(reverse = True)
    if len(valList) == 1:
        print('YES')
    elif valList[0] == valList[1]:
        print('NO')
    else:
        print('YES')
    t-=1
