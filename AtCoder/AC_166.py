#D問題
N,M = map(int,input().split())
H=list(map(int,input().split()))
A=[0]*M
B=[0]*M
for i in range(M):
    A[i],B[i]=map(int,input().split())
print(H)
print(A)
print(B)


#B問題
N,K=map(int,input().split())
list1=[]
for _ in range(K):
    s=int(input())
    list1.extend(list(map(int,input().split())))


list1=list(set(list1))
print(N-len(list1))

#C問題
X=int(input())
x=0
list=[]
for i in range(-118,120,1):
    for j in range(-119,119,1):
        x=i**5-j**5
        if x==X:
            print((str(i)+' '+str(j)))
            break
    else:
        continue
    break
