n = int(input())
m = int(input())
s = input()

result=0
str = 'IOI'+'OI'*(n-1)

for i in range(m):
    if s[i:i+len(str)]==str: result+=1
print(result)