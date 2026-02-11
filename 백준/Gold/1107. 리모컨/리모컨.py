import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
arr = list(input().split())
base = abs(n-100)

for i in range(1000001):
    for j in set(str(i)):
        if j in arr: break
    else: 
        base = min(base, len(str(i))+abs(int(i)-n))
print(base)