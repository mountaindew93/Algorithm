import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr=[]; per=[]; result=10000000000000000
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n): per.append(i)
all=set(per)
com = list(set(combinations(per,n//2)))

for i in range(len(com)):
    startr=0; remainr=0
    start = list(com[i])
    remain = list(all-set(start))
    for a, b in list(set(combinations(start,2))):
        startr+=arr[a][b]+arr[b][a]
    for a,b in list(set(combinations(remain, 2))):
        remainr+=arr[a][b]+arr[b][a]
    if abs(startr - remainr) < result:
        result = abs(startr - remainr)
print(result)