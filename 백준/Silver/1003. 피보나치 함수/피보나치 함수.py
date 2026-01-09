T = int(input())

for _ in range(T):
    zero=0; one=1; temp=0
    n = int(input())
    if n==0 : print(1, 0)
    else:
        for _ in range(n-1):
            temp=one
            one=zero+one
            zero=temp
        print(zero, one)