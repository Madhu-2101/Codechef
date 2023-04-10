# A football competition has just finished. The players have been given points for scoring goals and points for committing fouls. Now, it is up to Alex to find the best 
# player in the tournament. As a programmer, your job is to help Alex by telling him the highest number of points achieved by some player. You are given two sequences 
# A1,A2,…,AN and B1,B2,…,BN. For each valid i, player i scored Ai goals and committed Bi fouls. For each goal, the player that scored it gets 20 points, and for each 
# foul, 10 points are deducted from the player that committed it. However, if the resulting number of points of some player is negative, this player will be considered to 
# have 0 points instead. You need to calculate the total number of points gained by each player and tell Alex the maximum of these values.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

t=int(input())
while t>0:
    n=int(input())
    goals=list(map(int,input().split()))
    fouls=list(map(int,input().split()))
    points=[]
    for i in range(n):
        points.append(goals[i]*20-fouls[i]*10)
    print(max(points) if max(points)>0 else '0')
    t-=1
