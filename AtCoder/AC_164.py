#AC_164_D Multiple of 2019
S=input()
i=2019
x = 0
while i <= int(S):
    for j in range(1,len(S)-len(str(i))+2,1):
        if int(S[j-1:j-1+len(str(i))]) == i:
            x += 1
    i += 2019
print(x)
