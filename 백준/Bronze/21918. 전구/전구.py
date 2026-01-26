n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b-1] = c
    elif a == 2:
        for j in range(b-1, c):
            arr[j] = 1 - arr[j]
    elif a == 3:
        for j in range(b-1, c):
            arr[j] = 0
    elif a == 4:
        for j in range(b-1, c):
            arr[j] = 1

for z in arr:
    print(z, end=' ')
