import sys
input = sys.stdin.readline

n = int(input())
result = 0

for _ in range(n):
    word = input().strip()
    if list(word) == sorted(word, key=word.find):
        result += 1

print(result)