# 배열 단일 업데이트

n = input()

A = list(map(int, input().split()))

i, j, k = map(int, input().split())

for index in range(i, j + 1):
    A[index] = A[index] * k


print(sum(A))

# A의 i 번째 원소부터 A의 j 번째 원소에 k 를 곱한다.

# n=8, A=1 1 1 1 1 1 1 1, i=0, j=4, k=2