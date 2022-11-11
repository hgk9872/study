# 문제 틀림 나중에 다시 p347

s = "()))((()"

def check_balance(s):
    right = 0
    left = 0
    for c in s:
        if c == "(":
            left += 1
        else:
            right += 1
    if left == right:
        return True
    else:
        False

def transform(w):
    result = ''
    if w == "":
        return w
    for i in range(2, len(w)+1, 2):
        u = w[:i]
        v = w[i:]
        temp = ""
        if not check_balance(u): # 균형잡힌 문자열이 아니라면
            continue
        if check_right(u): # 올바른 문자열이라면
            result = u + transform(v)
        else: # 올바른 문자열이 아니라면
            temp = "(" + transform(v) + ")"
            u = u[1:-1]
            for j in u:
                if j == "(":
                    temp += ")"
                else:
                    temp += "("
            result = temp
    return result
def check_right(s):
    count = 0
    for char in s:
        if char == "(":
            count += 1
        else: # ")"
            count -= 1
            if count < 0:
                return False
    
    # 균형잡힌 문자열이라면 true
    if count == 0:
        return True
    else:
        return False

def solution(p):
    answer = transform(p)
    print(answer)
    return answer

solution(s)