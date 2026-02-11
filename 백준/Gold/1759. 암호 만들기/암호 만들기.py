import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int, input().split())
arr = list(input().split())
aa = ['a', 'i', 'e', 'o', 'u']; 
arr.sort()

for i in combinations(arr, n):
    jj=0; m=0
    for j in i:
        if j in aa: jj+=1
        else : m+=1
    if jj>=1 and m>=2: print(''.join(i))