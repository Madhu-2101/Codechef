# Chef and his friend is standing on the X-axis at the points X1 and X2 respectively. Chef moves one step forward each second (that is he moves to X1+1 after the
# 1st second, X1+2 after the 2nd second, and so on), whereas his friend moves 2 steps forward each second (that is he moves to X2+2 after the 1st second, X2+4 after
# the 2nd second, and so on). You need to determine if Chef will be able to meet his friend or not. You can assume that Chef and his friend both keep on moving for a long
# indefinite amount of time and also that they move simultaneously.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

t=int(input())
while t>0:
    x,y=map(int, input().split())
    if x>=y:
        print('YES')
    else:
        print('NO')
    t-=1
