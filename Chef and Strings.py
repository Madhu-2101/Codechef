# Having already mastered cooking, Chef has now decided to learn how to play the guitar. Often while trying to play a song, Chef has to skip several strings to reach
# the string he has to pluck. Eg. he may have to pluck the 1st string and then the 6th string. This is easy in guitars with only 6 strings; However, Chef is playing a 
# guitar with 10 6 strings. In order to simplify his task, Chef wants you to write a program that will tell him the total number of strings he has to skip while playing 
# his favourite song.
#  Eg. to switch from string 1 to 6, Chef would have to skip 4 strings (2,3,4,5).
 
 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int, input().split()))
    count=0
    for i in range(n-1):
        count+=(max(arr[i], arr[i+1])-min(arr[i], arr[i+1])-1)
    print(count)
    t-=1
