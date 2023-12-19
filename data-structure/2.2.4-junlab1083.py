# 특정 소문자를 대문자로 바꾸기

A = input()

B = list(map(str, input().split()))

result = ''

for i in A:
    if i in B:
        result += i.upper()
    else:
        result += i

print(result)