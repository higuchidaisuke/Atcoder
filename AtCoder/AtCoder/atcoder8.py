#AtCoder Beginner Contest 155 class
N=int(input())
S=[]
for _ in range(N):
    S.append(input())
S1=list(set(S))
C=[]
for i in S1:
    C.append(S.count(i))
D=[x for x in S1 if S.count(x) >=max(C)]
D.sort()
for i in D:
    print(i)
