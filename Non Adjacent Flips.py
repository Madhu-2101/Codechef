# You are given a binary string S of length N. You can perform the following operation on S: 
# Pick any set of indices such that no two picked indices are adjacent. Flip the values at the picked indices (i.e. change 0 to 1 and 1 to 0).
# For example, consider the string S=1101101.
# If we pick the indices {1,3,6}, then after flipping the values at picked indices, we will get 1101101 → 0111111. 
# Note that we cannot pick the set {2,3,5} since 2 and 3 are adjacent indices. Find the minimum number of operations required to convert all the characters of S to 0.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

for _ in range(int(input())):
    n = int(input())
    s = input()
    pairs = s.count('11')
    if '1' in s:
        if pairs > 0:
            print(2)
        else:
            print(1)
    else:
        print(0)
