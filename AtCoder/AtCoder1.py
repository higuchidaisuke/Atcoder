import math
import numpy
a,b,c = map(int, input().split())
if math.sqrt(a)+math.sqrt(b)<math.sqrt(c):
    print("Yes")
else:
    print("No")

import math
import numpy
a,b,c = map(int, input().split())
d = c - a - b
if d > 0 and d*d > 4 * a * b:
    print("Yes")
else:
    print("No")

N,R = map(int,input().split())
if N >= 10:
  print(R)
else:
  print(R+100*(10-N))
