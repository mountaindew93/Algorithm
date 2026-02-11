import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

n, s = map(int, input().split())
arr=list(map(int, input().split()))
result = arr.count(s)

for i in range(2,n+1):
    for j in list(combinations(arr,i)):
        if sum(j)==s: result+=1
print(result)