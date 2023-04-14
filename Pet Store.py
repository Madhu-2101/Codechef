# Alice and Bob went to a pet store. There are N animals in the store where the ith thanimal is of type Ai .
# Alice decides to buy some of these N animals. Bob decides that he will buy all the animals left in the store after Alice has made the purchase.
# Find out whether it is possible that Alice and Bob end up with exactly same multiset of animals.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    c = Counter(arr)
    for i in c.values():
        if i%2!=0:
            print('NO')
            break
    else:
        print('YES')
