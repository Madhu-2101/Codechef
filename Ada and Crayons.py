Ada has an array of N crayons, some crayons are pointing upwards and some downwards. Ada thinks that an array of crayons is beautiful if all the crayons are pointing 
in the same direction. In one step you can flip any segment of consecutive crayons. After flipping a segment, all crayons pointing downwards will point upwards and 
visceversa What is the minimum number of steps to make the array of crayons beautiful?

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

t=int(input())
while t>0:
    txt=input()
    s1=""+txt[0]
    for i in txt:
        if s1[-1]!=i:
            s1+=i
    print(min(s1.count("U"),s1.count("D")))
    t-=1
