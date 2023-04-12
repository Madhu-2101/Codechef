# Mathison recently inherited an ancient papyrus that contained some text. Unfortunately, the text was not a pangram. Now, Mathison has a particular liking
# for holoalphabetic strings and the text bothers him. The good news is that Mathison can buy letters from the local store in order to turn his text into a pangram.
# However, each letter has a price and Mathison is not very rich. Can you help Mathison find the cheapestway to obtain a pangram?

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

t = int(input())
while t>0:
    arr = list(map(int, input().split()))
    txt = input()
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    ans=0
    for i in range(len(alpha)):
        if alpha[i] not in txt:
            ans+=arr[i]
    print(ans)
    t-=1
