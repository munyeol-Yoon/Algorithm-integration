# 대문자 제거하기

A = input()
B = ''

for i in range(len(A)):
    if A[i].islower():
        B += A[i]

print(B)

'''
A: 알파벳 대소문자로 구성된 문자열
문자열 A에서 모든 대문자를 제거한 후 남은 소문자를 기존 순서대로 이어 붙인 문자열을 반환

def solution(A):
    # 문자열 A의 모든 문자 a를 탐색하면서 문자열 B를 만든다. (B: 정답 문자열 저장)
    B = ''
    for a in A:
        if a.islower():
            B += a
    return B

# 입력받고 정답을 출력한다.
A = input()
print(solution(A))

'''