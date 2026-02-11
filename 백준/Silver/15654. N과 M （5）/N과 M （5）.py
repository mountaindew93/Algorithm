import sys
from itertools import permutations
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for i in list(permutations(arr, m)):
    print(*i)