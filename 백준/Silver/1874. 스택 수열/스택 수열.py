import sys
input = sys.stdin.readline
n = int(input())
stk=[]; result=[]; cur=1

for i in range(n):
    num = int(input())
    while cur<=num:
        stk.append(cur)
        result.append('+')
        cur+=1

    if stk[-1]==num:
        stk.pop()
        result.append('-')
    else: print("NO"); exit()

for i in result:
    print(i)