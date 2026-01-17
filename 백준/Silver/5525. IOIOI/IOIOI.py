import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

result=0; chk=0; flag=0
str = 'IOI'

while(chk!=m):
    if s[chk:chk+3] == str:
        chk+=2; flag +=1
        if flag>=n: result+=1
    else: chk+=1; flag=0


print(result)