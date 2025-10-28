n=int(input())
for i in range(n,1,-1):
    flag=0
    for j in str(i):
        if j!='7' and j!='4':
            flag=1
            break
    if flag==0: 
        print(i); break