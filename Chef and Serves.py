# In a regular table tennis match, the player who serves changes every time after 2 points are scored, regardless of which players scored them. Chef and Cook are 
# playing a different match — they decided that the player who serves would change every time after K points are scored instead (again regardless of which players 
# scored them). When the game starts, it's Chef's turn to serve. You are given the current number of points scored by Chef and Cook (P1 and P2 respectively). 
# Find out whether Chef or Cook has to serve next.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

t=int(input())
while t>0:
    p1,p2,k=map(int,input().split())
    i=0
    sum=p1+p2
    while sum>=k:
        sum-=k
        i+=1
    if i%2==0:
        print('CHEF')
    else:
        print('COOK')
    t-=1
