sum=0; temp=200
arr=[]
for _ in range(10):
    n=int(input())
    sum+=n
    arr.append(sum)
for i in arr:
    if abs(100-i) <= abs(100-temp) :
        temp=i
print(temp)