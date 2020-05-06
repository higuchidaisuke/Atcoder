K=int(input())
def gcd(a,b,c):
    if a <b:
        a,b=b,a
    while a%b != 0:
        a,b= b,a%b
    if b < c:
        b,c=c,b
    while b % c != 0:
        b,c = c,b%c
    return c
x=0
for i in range(1,K+1):
    for j in range(1,K+1):

            for l in range(1,K+1):
                
                    if (i==1) or (j==1) or (l==1):
                        x+=1
                    else:
                        x += gcd(i,j,l)
print(x)
