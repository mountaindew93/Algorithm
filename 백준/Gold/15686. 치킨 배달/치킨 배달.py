import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()
n,m = map(int, input().split())
chicken=[]; home=[]

for i in range(n):
    llt = list(map(int, input().split()))
    for j in range(n):
        if llt[j]==1: home.append((i,j))
        elif llt[j]==2:chicken.append((i,j))

rresult=100000000000
for i in list(combinations(chicken, m)):
    result=0
    for a,b in home:
        temp=1000000000000
        for x,y in i:
            if abs(x-a)+abs(y-b)<temp:
                temp=abs(x-a)+abs(y-b)
        result+=temp
    rresult=min(result, rresult)

print(rresult)