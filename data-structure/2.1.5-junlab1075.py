# 2차원 배열 단일 업데이트

n = int(input())

A = list(list(map(int, input().split())) for _ in range(n))

i1, j1, i2, j2, k = map(int, input().split())


for i in range(i1, i2 + 1):
    for j in range(j1, j2 + 1):
        A[i][j] = A[i][j] * k

answer = 0
for i in range(n):
    answer += sum(A[i])

print(answer)

'''
저자 답

# n, A: 크기가 n x n 인 정수형 2차원 배열 A
# i1, j1, i2, j2, k : 행 번호가 i1~i2 이고 열 번호가 j1~j2인 배열 A의 원소에 k를 곱하는 연산을 수행
# 연산을 수행한 후 배열 A의 모든 원소의 합을 반환한다.

def solution(n, A, i1, j1, i2, j2, k):
    # 행 번호가 i1~i2, 열 번호가 j1~j2 인 배열 A의 모든 원소에 k를 곱하는 연산을 수행한다.
    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):
            A[i][j] = A[i][j] * k
    
    # 배열 A의 모든 원소의 합을 행 단위로 계산
    answer = 0
    for i in range(n):
        answer += sum(A[i])
    
    return answer

n = int(input())
A = list(list(map(int, input().split())) for _ in range(n))
i1, j1, i2, j2, k = map(int, input().split())
print(solution(n, A, i1, j1, i2, j2, k))


'''