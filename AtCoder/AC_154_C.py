N=int(input())
A=list(map(int,input().split()))

if len(list(set(A)))==N:
    print('YES')
else:
    print("NO")
