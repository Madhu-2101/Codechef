# Apple considers any iPhone with a battery health of 80% or above, to be in optimal condition. Given that your iPhone has X% battery health, find whether it is in optimal 
# condition.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

t=int(input())
while t>0:
    x=int(input())
    print('YES' if x>=80 else 'NO')
    t-=1
