# 2차원 배열 원소 개수 구하기

n, k = map(int, input().split())

A = []

answer = 0

for j in range(n):
    row = list(map(int, input().split()))
    A.append(row)


for i in range(n):
    for j in range(n):
        if A[i][j] == k:
            answer += 1

print(answer)

'''
저자 답

def solution(n, A, k):
    answer = 0
    for i in range(n):
        for j in range(n):
            if A[i][j] == k:
                answer += 1
    return answer

n, k = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(n))
print(solution(n, A, K))

'''