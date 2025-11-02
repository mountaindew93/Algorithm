n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if arr[j][i]==1 and arr[i][k]==1:
                arr[j][k] = 1
for j in arr:
    print(*j)