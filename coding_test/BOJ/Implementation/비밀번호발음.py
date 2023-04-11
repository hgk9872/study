# https://www.acmicpc.net/problem/4659 s5

# 반드시 하나 포함
required = ['a', 'e', 'i', 'o', 'u']

# 모음 반드시 하나 포함
def check1(word):
    for i in range(len(word)):
        # 하나라도 있는 경우 True
        if word[i] in required:
            return True
    return False

# 모음 혹은 자음이 연속으로 오는지 체크
def check2(word):
    count1 = 0
    count2 = 0

    for i in range(len(word)):
        if word[i] in required: # 모음
            count1 += 1
            count2 = 0
        else: # 자음
            count2 += 1
            count1 = 0
        if count1 == 3 or count2 == 3:
            return False
    return True

def check3(word):
    prev = word[0]
    count = 1

    for i in range(1, len(word)):
        if word[i] == prev:
            count += 1
        else:
            prev = word[i]
            count = 1
        # 연속으로 3개 오는 경우
        if count == 2:
            if prev == 'e' or prev == 'o':
                return True
            else:
                return False
    return True


while True:
    word = input()
    if word == 'end':
        break
    if not check1(word):
        print(f'<{word}> is not acceptable.')
        continue
    if not check2(word):
        print(f'<{word}> is not acceptable.')
        continue
    if not check3(word):
        print(f'<{word}> is not acceptable.')
        continue
    print(f'<{word}> is acceptable.')