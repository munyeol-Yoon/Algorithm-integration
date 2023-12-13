# 배열 원소 개수 구하기

n, k = map(int, input().split())

A = list(map(int, input().split()))

answer = 0

for i in A:
    if i == k:
        answer+=1

print(answer)