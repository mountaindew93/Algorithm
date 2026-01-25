import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

stk=[]; result=[]
stk.append((arr[0],1))
result.append(0)

for i in range(1, n):
    while stk and arr[i]>stk[-1][0]:
        stk.pop()

    if not stk : result.append(0)
    else : 
        result.append(stk[-1][1])
    stk.append((arr[i], i+1))
print(*result)