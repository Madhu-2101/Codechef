# You are given an array A of N positive and pairwise distinct integers. You can permute the elements in any way you want. The cost of an ordering (A1,A2,…,An) is 
# defined as mod (((A1 mod A2) mod A3)......) mod An where mod X mod Y means the remainder when X is divided by Y. You need to find the maximum cost which can be attained 
# through any possible ordering of the elements.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=min(arr[0],arr[1])
    for i in range(2,n):
        ans=min(ans,arr[i])
    print(ans)
