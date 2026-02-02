import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
stack =[]; result=[]

arr = list(map(int, input().split()))
stack.append(arr[n-1]); result.append(-1)

for i in range(n-2, -1, -1):
    flag=0
    while(stack):
        if stack[-1]>arr[i]:
            result.append(stack[-1])
            stack.append(arr[i])
            flag=1
            break
        else:
            del(stack[-1])
    if not flag:
        result.append(-1)
        stack.append(arr[i])
    
result.reverse()
print(*result)