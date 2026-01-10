import math
n = int(input())
result=0

fac = str(math.factorial(n))
for i in range(1, len(fac)+1):
    if fac[-i] == '0' : result+=1
    else: break
print(result)