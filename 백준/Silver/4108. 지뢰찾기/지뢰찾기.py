while(True):
    r, c = map(int, input().split())
    if r==0 and c==0: break
    arr=[]; chk = [[-1,-1], [-1, 0 ], [-1, 1], [0,-1], [0,1],[1,-1],[1,0],[1,1]]
    result=[['' for _ in range(c)] for _ in range(r)]

    for _ in range(r):
        arr+=list(input().split())

    for i in range(r):
        for j in range(c):
            x=i; y=j
            if arr[i][j] == '*':
                result[i][j]='*'
            else:
                sum=0
                for x,y in chk:
                    if 0<=i+x<r and 0<=j+y<c:
                        if arr[i+x][j+y]=='*':
                            sum+=1
                result[i][j]=str(sum)
    for i in result:
        print(''.join(i))