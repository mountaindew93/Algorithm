import sys
input = sys.stdin.readline

def dfs (sum, dic):
    for key in sorted(dic.keys()):
        print(sum*'--'+key)
        dfs(sum+1, dic[key])    
    
dic = {}; sum=0

n = int(input())
for _ in range(n):
    arr = list(input().strip().split())
    cur = dic
    for i in range(1, int(arr[0])+1):
        cur = cur.setdefault(arr[i], {})

dfs(sum, dic)
