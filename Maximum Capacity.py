# A building lift has a maximum capacity of 500 kilograms. However, due to the pandemic, at most 8 people can use the lift at once.
# There are X friends, each having a weight of Y kilograms. Find whether all of them can use the lift at once.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

t = int(input())
while t>0:
    x,y = map(int, input().split())
    if x<=8 and x*y<=500:
        print("YES")
    else:
        print("NO")
    t-=1
