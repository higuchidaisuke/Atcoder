import math

A,B,N=map(int,input().split())

if B==1:
    print(0)
else:
    if B > N:
        print(math.floor(A*N/B))

    else:
        print(math.floor(A*(B-1)/B))
