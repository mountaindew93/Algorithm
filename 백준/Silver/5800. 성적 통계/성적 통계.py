import sys
input = sys.stdin.readline


arr = []
kk = int(input())
for k in range(kk):
    temp=0
    arr = list(map(int, input().split()))
    num = arr.pop(0)
    arr = sorted(arr, reverse=True)
    for i in range(num-1):
        if arr[i]-arr[i+1] > temp:
            temp = arr[i]-arr[i+1]
    print("Class", k+1)
    print("Max %d, Min %d, Largest gap %d" % (max(arr), min(arr), temp))
