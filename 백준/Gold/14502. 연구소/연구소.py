import sys
import copy
from itertools import combinations

def dfs(temp, x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                dfs(temp, nx, ny)

input = lambda: sys.stdin.readline().rstrip()
n,m = map(int, input().split())
arr =[]; zero=[]; zone=0; vir=[]
for _ in range(n): arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if arr[i][j]==0: zero.append((i,j))
        elif arr[i][j]==2: vir.append((i,j))

for i in list(combinations(zero, 3)):
    search = copy.deepcopy(arr)
    for x,y in i: search[x][y]=1
    for a,b in vir:
        dfs(search, a,b)
    zone = max(zone, sum(row.count(0) for row in search))
print(zone)