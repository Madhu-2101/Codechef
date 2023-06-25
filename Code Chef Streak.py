# CodeChef offers a feature called streak count. A streak is maintained if you solve at least one problem daily. Om and Addy actively maintain 
# their streaks on CodeChef. Over a span of N consecutive days, you have observed the count of problems solved by each of them.Your task is to 
# determine the maximum streak achieved by Om and Addy and find who had the longer maximum streak.


for _ in range(int(input())):
    n = int(input())
    om = list(map(int, input().split()))
    addy = list(map(int, input().split()))
    oc=0
    omc=0
    ac = 0
    amc = 0
    for i in range(n):
        if om[i]!=0:
            oc+=1
        else:
            oc=0
        if omc < oc:
            omc=oc
        if addy[i]!=0:
            ac+=1
        else:
            ac=0
        if amc < ac:
            amc=ac
    if omc==amc:
        print('Draw')
    elif amc>omc:
        print('Addy')
    else:
        print('Om')
  
    
