# Chef is going on a road trip and needs to apply for inter-district and inter-state travel e-passes. It takes A minutes to fill each inter-district e-pass application 
# and B minutes for each inter-state e-pass application. His journey is given to you as a binary string S of length N where 0 denotes crossing from one district to another 
# district (which needs an inter-district e-pass), and 1 denotes crossing from one state to another (which needs an inter-state e-pass). Find the total time Chef has to 
# spend on filling the various forms.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

for _ in range(int(input())):
    n,a,b = map(int, input().split())
    s = input()
    zero_count = s.count('0')
    one_count = s.count('1')
    print(zero_count*a + one_count*b)
