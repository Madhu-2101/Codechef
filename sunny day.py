# Chef is planning a family picnic. He will go to the picnic only if the temperature on that day is strictly greater than 24 degrees.
# Given that the temperature on a day is X degrees, find whether he will go to the picnic on that day.

-----------------------------------------------------------------------------------------------------------------------------

t = int(input())
while t>0:
    x = int(input())
    if x>24:
        print("YES")
    else:
        print("NO")
    t-=1
