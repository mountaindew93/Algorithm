t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    sum = 0
    for i in range(n, m+1):
        for j in str(i):
            if '0' == j : sum+=1 
    print(sum)