## 문자열 뒤집기 코딩 (파이썬)
origin_str = 'Life is short'

# 1. slicing
reversed_str1 = origin_str[::-1]
print(reversed_str1) # str format

# 2. reversed() func
# reversed()는 iterator 데이터 (not string)
reversed_str2 = ''.join(reversed(origin_str))
print(reversed_str2)