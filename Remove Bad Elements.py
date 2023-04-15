# Chef has an array A of length N. In one operation, Chef can remove any one element from the array. Determine the minimum number of operations required to make all 
# the elements same.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from collections import Counter
t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int, input().split()))
    c=Counter(arr)
    print(n-max(c.values()))
    t-=1
