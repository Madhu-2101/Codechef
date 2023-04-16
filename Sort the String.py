# You have a binary string S of length N. In one operation you can select a substring of S and reverse it. For example, on reversing the substring S[2,4] for S=11000, 
# we change 11000→10010. Find the minimum number of operations required to sort this binary string. It can be proven that the string can always be sorted using the above 
# operation finite number of times.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

for _ in range (int(input())):
    t=int(input())
    s=input()
    m=0
    for i in range(t-1):
        if s[i]=='1'and s[i+1]=='0':
            m+=1
    print(m)
