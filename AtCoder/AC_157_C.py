#解法１
N,M=map(int,input().split())
s=[]
c=[]
for i in range(M):
    a,b=map(int,input().split())
    s.append(a)
    c.append(b)
found=False
start=pow(10,N-1)
stop=pow(10,N)
if N==1:
    start=0
for i in range(start,stop):
    i_str=str(i)
    passed=True
    for j in range(M):
        if not i_str[s[j]-1]==str(c[j]):
            passed=False
            break
    if passed:
        found=True
        print(i)
        break
if not found:
    print('-1')


#解法２
N,M=map(int,input().split())
s=[]
c=[]
for i in range(M):
    a,b=map(int,input().split())
    s.append(a)
    c.append(b)
okflag=True

for i in range(M):
    if not okflag:
        break

    for j in range(M):
        if not okflag:
            break
        if not (i==j):

            if s[i]=s[j] and c[i] != c[j]:
                okflag=False
                print('-1')


if okflag:

    answer=["x"]*N
    for
