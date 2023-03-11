def solution(s):
    stack = []

    for i in range(len(s)):
        # 스택이 비어있는 경우
        if not stack:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])