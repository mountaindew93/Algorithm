import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())

for _ in range(n):
    s = input()
    num = int(input())
    arr = input()
    arr= arr[1:-1].split(',')
    flip=0; front=0; flag=0; rear=num

    for i in s:
        if i=='R': flip = 1-flip
        elif i=='D':
            if rear<=front : print("error"); flag=1; break
            if flip: rear-=1
            else : front+=1

    if not flag : 
        if flip: 
            arr = arr[front:rear]
            arr.reverse()
            print("[" + ','.join(arr) + "]")
        else : 
            print("[" + ','.join(arr[front:rear]) + "]")