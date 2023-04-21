# Not everyone probably knows that Chef has younger brother Jeff. Currently Jeff learns to read. He knows some subset of the letter of Latin alphabet. In order to help 
# Jeff to study, Chef gave him a book with the text consisting of N words. Jeff can read a word iff it consists only of the letters he knows. Now Chef is curious about 
# which words his brother will be able to read, and which are not. Please help him!

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

s=input()
for _ in range(int(input())):
    w=input()
    for i in w:
        if i not in s:
            print('No')
            break
    else:
        print('Yes')
    
