# The Chef likes to stay in touch with his staff. So, the Chef, the head server, and the sous-chef all carry two-way transceivers so they can stay 
# in constant contact. Of course, these transceivers have a limited range so if two are too far apart, they cannot communicate directly. The Chef 
# invested in top-of-the-line transceivers which have a few advanced features. One is that even if two people cannot talk directly because they are
# out of range, if there is another transceiver that is close enough to both, then the two transceivers can still communicate with each other using 
# the third transceiver as an intermediate device. There has been a minor emergency in the Chef's restaurant and he needs to communicate with both 
# the head server and the sous-chef right away. Help the Chef determine if it is possible for all three people to communicate with each other,
# even if two must communicate through the third because they are too far apart.


import math
def dis(a1, a2, b1, b2):
    return ((a1-a2)**2+(b1-b2)**2)

t = int(input())
while t > 0:
    
    R = int(input())
    X, Y = [], []
    for i in range(3):
        a, b = list(map(int, input().split()))
        X.append(a)
        Y.append(b)
    dis1 = dis(X[0], X[1], Y[0], Y[1])
    dis2 = dis(X[1], X[2], Y[1], Y[2])
    dis3 = dis(X[2], X[0], Y[2], Y[0])
    
    total_d = dis1+dis2+dis3
    second_d = total_d - max(dis1, dis2, dis3) - min(dis1, dis2, dis3)
    
    if second_d <= R**2:
        print("yes")
    else:
        print("no")
    
    
    
    t -= 1
