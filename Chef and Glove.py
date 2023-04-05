# Winter has finally come to Chefland, so Chef bought a glove for herself. Chef has a hand with N fingers (for the sake of simplicity, let us consider the thumb a finger 
# too) numbered 1 through N and the glove has N sheaths numbered 1 through N. Exactly one finger has to be inserted into each sheath. You are given the lengths of Chef's 
# fingers, as seen from left to right. You are also given the lengths of the sheaths of the glove, from left to right, as seen from the front. Chef can wear the glove 
# normally (the front side of the glove matching the front of Chef's hand), or she can flip the glove and then insert her hand in it. In the first case, the first finger 
# will go into the first sheath, the second finger into the second one, and so on. However, when she flips the glove, her first finger will go into the N-th sheath, the 
# second finger into the (N-1)-th and so on — the i-th finger will go into the N+1-i-th sheath for each valid i. Of course, for her to wear the glove comfortably, each 
# finger's length should be less than or equal to the length of the sheath it goes into. Find out whether Chef can wear the glove by keeping its front side facing her, or 
# if she can wear it by flipping it over and facing its back side. If she can only wear the glove in the former way, output "front"; if she can wear it only in the latter 
# way, output "back". If both front and back orientations can be used, output "both", and if she can't wear it either way, output "none".

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

t=int(input())
while t>0:
    n=int(input())
    l=list(map(int,input().split()))
    g=list(map(int,input().split()))
    b=n-1
    front,back=True,True
    for i in range(n):
        if l[i]>g[i]:
            front=False
        if l[b]>g[i]:
            back=False
        b-=1
    if front and back:
        print('both')
    elif front:
        print('front')
    elif back:
        print('back')
    else:
        print('none')
    t-=1
