We have found a new chess character — pook. It has the qualities of both a rook and a pawn. Specifically, treating the chessboard to be an N×N grid where (i,j) denotes 
the intersection of the i-th row and the j-th column, a pook placed at square (x,y) threatens the following squares:
(i,y) for every 1≤i≤N 
(x,i) for every 1≤i≤N 
(x+1,y−1), if x<N and y≥2 
(x+1,y+1), if x<N and y<N 
Find the maximum number of pooks that can be placed on an empty N×N chessboard such that none of them threaten each other.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

for _ in range(int(input())):
    n = int(input())
    print(n if n > 3 else n-1 if n>1 else 1)
