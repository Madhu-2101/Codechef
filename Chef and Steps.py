# In order to establish dominance amongst his friends, Chef has decided that he will only walk in large steps of length exactly K feet. However, this has presented 
# many problems in Chef’s life because there are certain distances that he cannot traverse. Eg. If his step length is 5 feet, he cannot travel a distance of 12 feet. 
# Chef has a strict travel plan that he follows on most days, but now he is worried that some of those distances may become impossible to travel. Given N distances, 
# tell Chef which ones he cannot travel.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

t=int(input())
while t>0:
    n,x=map(int, input().split())
    arr = list(map(int, input().split()))
    ans=''
    for i in arr:
        if i%x==0:
            ans+='1'
        else:
            ans+='0'
    print(ans)
    t-=1
