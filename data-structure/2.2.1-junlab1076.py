# 짝수 번째 문자열

# 문자열 짝수만 출력

A = input()
B = ''

for i in range(1, len(A), 2):
    B += A[i]

print(B)

'''
저자 답

# A: 알파벳 대소문자로 구성된 문자열
# 문자열 A에서 홀 수 번째 문자를 모두 제거한 후 남은 문자열을 기존 순서를 유지하면서 이어 붙인 문자열을 반환한다.

def solution(A):
    B = A[1::2]
    return B

A = input()
print(solution(A))

'''