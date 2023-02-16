# 프로그래머스 문제 기반
# https://school.programmers.co.kr/learn/courses/30/lessons/12950

## 크기가 동일한 행렬 arr1, arr2를 더하는 방법
#   arr1      arr2
#  [[1,2],   [[3,4],
#   [2,3]]    [5,6]]	


def solution(arr1, arr2):
    for i in range(len(arr1)): # 행마다 반복
        for j in range(len(arr1[i])): # 해당 행의 열마다 반복
            arr1[i][j] += arr2[i][j]
    return arr1
