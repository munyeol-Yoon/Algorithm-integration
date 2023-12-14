# 소문자 제거하기

A = input()
B = ''

for i in range(len(A)):
    if A[i].isupper():
        B += A[i]

print(B)