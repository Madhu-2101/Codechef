# Given an alphanumeric string made up of digits and lower case Latin characters only, find the sum of all the digit characters in the string.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

for _ in range(int(input())):
    s = input()
    x = [int(s[i]) for i in range(len(s)) if s[i].isnumeric()]
    print(sum(x))
