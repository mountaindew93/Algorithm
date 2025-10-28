n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    arr = sorted(arr)
    summ = arr[0]+arr[1]
    arr[0]=summ; arr[1]=summ

print(sum(arr))