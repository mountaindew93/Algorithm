import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input()
    n = int(input())
    dic = {}
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = []
        dic[s[i]].append(i)
    arr = dic.values()
    som = []
    for i in arr:
        if len(i)<n:continue
        else : 
            for j in range(len(i)-n+1):
                som.append(i[j+n-1]-i[j]+1)
    if som:
        print(min(som), max(som))
    else : print(-1)
