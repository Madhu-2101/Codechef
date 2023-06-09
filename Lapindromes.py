# Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character.
# If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two 
# halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome.
# The two halves contain the same characters but their frequencies do not match. Your task is simple. Given a string, you need to tell if it is a lapindrome.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from collections import Counter
t = int(input())
while t>0:
    txt = input()
    txt1 = txt[:int(len(txt)/2)]
    if len(txt)%2 == 0:
        txt2 = txt[int(len(txt)/2):]
    else:
        txt2 = txt[int(len(txt)/2)+1:]
    c1 = Counter(txt1)
    c2 = Counter(txt2)
    for i in c1.keys():
        if c1[i] != c2[i]:
            print('NO')
            break
    else:
        print('YES')
    t-=1
