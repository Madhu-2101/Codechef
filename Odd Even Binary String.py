# Chef had an array A of length N such that 1 ≤ Ai ≤ N for all 1 ≤ i ≤ N. Chef constructed another binary array B of length N in the following manner: 
# Bi=1 if the frequency of element i in A is odd. 
# Bi=0 if the frequency of element i in A is even. 
# Such an array B is called the parity encoding array of A. For example, if A=[1,1,2,3], then B=[0,1,1,0]. Unfortunately, Chef completely forgot the array A and 
# vaguely remembers the parity encoding array B. He is now wondering whether there exists any valid array A for which the parity encoding array is B. Can you help Chef?

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int, input().split()))
    if n%2 == sum(arr)%2:
        print("YES")
    else:
        print("NO")
    t-=1
