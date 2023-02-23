
temp = []
num = 10

while num > 0:
    temp.append(str(num % 2))
    num = num // 2

# 리스트를 문자열로 만들기
result = ''.join(temp)

# 문자열 뒤집기
print(result[::-1])