import sys
from itertools import permutations
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
num = list(map(int, input().split()))
cul = list(map(int, input().split()))
arr=[]; min=10000000000000; max=-10000000000000000000

for idx, i in enumerate(cul):
    if i > 0: arr.extend([idx]*i)

for i in list(set(permutations(arr,n-1))):
    m=1; sum=num[0]
    for j in list(i):
        if j==0: sum += num[m]
        elif j==1: sum -= num[m]
        elif j==2: sum *= num[m]
        elif j==3: sum=int(sum/num[m])
        m+=1
    if min>sum : min=sum
    if max<sum : max=sum
print(max)
print(min)