n,m = map(int, input().split())
arr = [input() for _ in range(n)]
cnt = []


for i in range(n-7):
    for j in range(m-7):
        cntB=0; cntW=0
        for col in range(i, i+8):
            for row in range(j, j+8):
                if (col+row)%2==0 :
                    if arr[col][row] == 'W' : cntB+=1
                    elif arr[col][row] == 'B' : cntW+=1
                else: 
                    if arr[col][row] == 'W' : cntW+=1
                    elif arr[col][row] == 'B' : cntB+=1
        cnt.append(min(cntB, cntW))

print(min(cnt))