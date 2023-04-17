# A binary string is called alternating if no two adjacent characters of the string are equal. Formally, a binary string T of length M is called alternating if T ≠ Ti+1 
# for each 1≤i<M. For example, 0, 1, 01, 10, 101, 010, 1010 are alternating strings while 11, 001, 1110 are not. You are given a binary string S of length N. 
# You would like to rearrange the characters of S such that the length of the longest alternating substring of S is maximum. Find this maximum value. A binary string is 
# a string that consists of characters 0 and 1. A string a is a substring of a string b if a can be obtained from b by deletion of several (possibly, zero or all) 
# characters from the beginning and several (possibly, zero or all) characters from the end.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

for _ in range(int(input())):
    n = int(input())
    s = input()
    ones = s.count('1')
    zeros = n - ones
    pairs = 2*min(ones,zeros)
    extra = min(abs(zeros - ones),1)
    print(pairs + extra)
