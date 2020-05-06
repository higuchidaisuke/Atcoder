N,K=map(int,input().split())
H=list(map(int,input().split()))
H.sort(reverse=True)
count=0
if N <= K:
    print(0)
else:
    for i in H[K:]:
        count += i
    print(count)


if B >= N:
    print(math.floor(A*N/B))
else:
    for x in range(B+1,N+1):
        y=math.floor(A*(B-1)/B)
        if math.floor(A*x/B)-A*math.floor(x/B) > y:
            y= math.floor(A*x/B)-A*math.floor(x/B)


    print(y)



A,B,C,D=map(int,input().split())
while A and C > 0: #最初＆にしていたためできなかった
    C -= B
    if C <= 0:
        print('Yes')
        break
    else:
        A -= D
        if A <=0:
            print('No')
            break

N=int(input())
list1=[]
for _ in range(N):
    list1.append(input())
print(len(list(set(list1))))
