# Chef has been searching for a good motivational movie that he can watch during his exam time. His hard disk has X GB of space remaining. His friend has N movies 
# represented with (Si,Ri) representing (space required, IMDB rating). Help Chef choose the single best movie (highest IMDB rating) that can fit in his hard disk.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

t=int(input())
while t>0:
    n,x=map(int, input().split())
    max=0
    for i in range(n):
        s,r=map(int, input().split())
        if s<=x and r>max:
            max=r
    print(max)
    t-=1
