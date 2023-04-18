t = int(input())
while t>0:
    N = int(input())
    list=[]
    A = input()
    B = input()
    for i in range(N):
        if A[i] != B[i]:
            if B[i] not in list:
                list.append(B[i])
    print(len(list))
    t-=1
