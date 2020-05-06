#Atcoder 158 C
A,B = list(map(int,input().split()))

found=False

for i in range(1010):
    A_tax=int(i*0.08)
    B_tax=int(i*0.10)

    if A==A_tax and B==B_tax:
        print(i)
        found=True
        break
if not found:
    print("-1")
