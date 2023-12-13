# 두 배열 원소 크기 비교

# n 개의 정수가 저장된 배열 A, B 가 주어짐, A의 인덱스와 B의 인덱스가 비교해 A의 원소가 더 큰경우의 수가 a, B 가 더큰경우 b

A = list(map(int, input().split()))
B = list(map(int, input().split()))

a, b = 0, 0

for i in range(len(A)):
    if A[i] > B[i]:
        a += 1
    elif A[i] < B[i]:
        b += 1

print(int(a > b))




    