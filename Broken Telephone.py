# Chef is judging a game called "Broken telephone". There are total N players taking part in the game. They are all sitting in a line. In the start of the game,
# first player is given a secret message written on a sheet of paper. Then they keep sending the message by whispering it to the player sitting immediate right to
# one and so on until it reaches the last person. Finally, the message received by the last player is compared with the message said by first player.
# If these messages aren't equal, there is someone who has misheard the message or whispered it wrongly to the next player. If messages is equal, then the players win
# and receive a tasty chocolate. Note that first player receives the message on a sheet of paper, thus he cannot mishear it.
# As Chef wants to be sure that every player has fulfilled his/ her role in the game, so he asks everyone to state their received messages after the end of the game.
# You are given an array A of N integers denoting messages received by each person.
# Please help Chef to find the number of players that could mishear the message or whisper it wrongly.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

t = int(input())
while t>0:
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i==0:
            if arr[i]!=arr[i+1]:
                ans+=1
        elif i>0 and i<n-1:
            if arr[i]==arr[i+1]==arr[i-1]:
                ans = ans
            else:
                ans+=1
        elif i==n-1:
            if arr[i]!=arr[i-1]:
                ans+=1
    print(ans)
    t-=1
