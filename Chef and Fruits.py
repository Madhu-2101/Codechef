# Today is Chef's birthday. His mom has surprised him with truly fruity gifts: 2 fruit baskets. The first basket contains N apples, and the second one contains M oranges. 
# Chef likes apples and oranges very much but he likes them equally, and therefore, wants to have the minimum possible difference between the number of apples and oranges 
# he has. To do so, he can purchase 1 apple or 1 orange by paying exactly 1 gold coin (that's some expensive fruit, eh?). Chef can purchase fruits at most K times (as he 
# has only K gold coins in his pocket) to make the difference the minimum possible. Our little Chef is busy in celebrating his birthday to the fullest, and therefore, he 
# has handed this job to his best friend — you. Can you help him by finding the minimum possible difference he can achieve between the number of apples and orange he owns?

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

for _ in range(int(input())):
    n, m, k = map(int,input().split())
    print(max(abs(n-m)-k,0))
