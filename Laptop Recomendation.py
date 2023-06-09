# Chef wants to buy a new laptop. However, he is confused about which laptop to buy out of 10 different laptops. He asks his N friends for their recommendation.
# The ℎ ith friend recommends the Chef to buy the ℎA ith laptop (1≤10)(1≤Ai≤10).Chef will buy the laptop which is recommended by maximum number of friends.
# Determine which laptop Chef buys.
# Print CONFUSED if there are multiple laptops having maximum number of recommendations.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from collections import Counter
for _ in range(int(input())):
    n = int(input())
    t = Counter(input().split()).most_common(2)
    if len(t) == 2:
        print(t[0][0] if t[0][1]>t[1][1] else 'CONFUSED')
    else:
        print(t[0][0])
