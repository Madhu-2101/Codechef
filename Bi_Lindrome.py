# You are given a string S of length N. Your task is to delete a subsequence of maximum length from the string, such that, after concatenating the remaining parts of the 
# string, it becomes a palindrome of length greater than 1. If this is possible, print the maximum length of the subsequence that can be deleted. Otherwise, print −1.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

t=int(input())
while t>0:
    n=int(input())
    s=input()
    s1=set(s)
    if len(s1)==len(s):
        print(-1)
    else:
        print(len(s)-2)
    t-=1
