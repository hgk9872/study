# BOJ 9251 - LCS
# dp

# 첫 번째 리스트
arr1 = list(input())

# 두 번째 리스트
arr2 = list(input())

# dp 테이블
dp = [0] * len(arr2)

#### 조건문에서, 문자열이 같은지에 대해 먼저 비교를 하면 틀림
#### 값이 누적변수의 값(cnt)가 추가되지 않는 케이스가 존재
#### 참고자료 : https://myjamong.tistory.com/317

# for i in range(len(arr1)):
#     cnt = 0
#     for j in range(len(arr2)):
#         if cnt < dp[j]:
#             cnt = dp[j]
#         elif arr2[j] == arr1[i]:
#             dp[j] = cnt + 1

for i in range(len(arr1)):
    cnt = 0
    for j in range(len(arr2)):
        if arr2[j] == arr1[i]:
            dp[j] = cnt + 1
        elif cnt < dp[j]:
            cnt = dp[j]

print(max(dp))