# 홀 수 번째 문자열

A = input()
B = ''

for i in range(0, len(A), 2):
    B += A[i]

print(B)