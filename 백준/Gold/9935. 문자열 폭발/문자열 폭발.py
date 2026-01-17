import sys
input = sys.stdin.readline

s= input().strip()
boom = input().strip()
stk = []

for i in s:
    stk.append(i)
    if list(boom) == stk[-len(boom):]:
        del stk[-len(boom):]

if not stk : print("FRULA")
else : print(''.join(stk))
