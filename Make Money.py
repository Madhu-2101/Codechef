# Chef has N bags and an integer X. The ith bag contains coins such that Ai≤X. In one operation, Chef can: 
# Pick any bag and increase its coins to X. Formally, if he choses the ith bag, he can set Ai=X. 
# Given that the cost of performing each operation is C (C≤X) coins and Chef can perform the above operation any (possibly zero) number of times, determine the 
# maximum value of: $\sum_{i=1}^N A_i$ $-$ total cost paid by Chef, if Chef performs the operations optimally.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

t=int(input())
while t>0:
    n,x,c=map(int,input().split())
    arr=list(map(int,input().split()))
    count=0
    for i in range(n):
        if arr[i]<x and (x-arr[i])>c:
            arr[i]=x
            count+=1
    print(sum(arr)-count*c)
    t-=1              
