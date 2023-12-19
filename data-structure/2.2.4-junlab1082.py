# 특정 대문자를 소문자로 바꾸기

A = input()

B = list(map(str, input().split()))

result = ''

for i in A:
    if i in B:
        result += i.lower()
    else:
        result += i
    

print(result)

'''
# A : 알파벳 대소문자로 구성된 문자열
# B : 알파벳 대문자를 원소로 갖는 1차원 배열
# 배열 B에 존재하는 모든 대문자 b에 대해 문자열 A에 존재하는 대문자 b 를 b에 대응하는 소문자로 치환한 문자열을 반환

def solution(A, B):
    # 배열 B에 있는 모든 대문자 b를 탐색한다.
    for b in B:
        # 문자열 A에 존재하는 대문자 b를 b에 대응하는 소문자로 치환한다.
        A = A.replace(b, b.lower())
    
    return A

A = input()
B = list(map(str, input()))
print(solution(A, B))

'''