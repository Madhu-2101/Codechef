# Chef has a number D containing only digits 0's and 1's. He wants to make the number to have all the digits same. For that, he will change exactly one digit, 
# i.e. from 0 to 1 or from 1 to 0. If it is possible to make all digits equal (either all 0's or all 1's) by flipping exactly 1 digit then output "Yes", else print "No" 
# (quotes for clarity)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

for _ in range(int(input())):
    d = input()
    one_count = d.count('1')
    zero_count = d.count('0')
    if zero_count==1 or one_count==1:
        print('Yes')
    else:
        print('No')
