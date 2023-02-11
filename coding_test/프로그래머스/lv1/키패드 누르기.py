# https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    # pad 리스트를 만들고, 리스트의 인덱스 자체를 숫자로 생각해서 풀이
    # 키패드에 해당하는 좌표 # 10(*), 12(#)
    pad = [[3, 1],
            [0,0], [0,1], [0,2],
           [1,0], [1, 1], [1, 2],
           [2, 0], [2, 1], [2, 2],
           [3, 0], [0], [3, 2],
          ]
    
    # 초기 위치
    cur_left = 10
    cur_right = 12
    
    answer = ''
    
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            cur_left = i
        elif i in [3, 6, 9]:
            answer += 'R'
            cur_right = i
        else:
            # 각각의 거리를 구해서 비교
            dist_left = abs(pad[i][0] - pad[cur_left][0]) + abs(pad[i][1] - pad[cur_left][1])
            dist_right = abs(pad[i][0] - pad[cur_right][0]) + abs(pad[i][1] - pad[cur_right][1])
            if dist_left < dist_right:
                answer += 'L'
                cur_left = i
            elif dist_left > dist_right:
                answer += 'R'
                cur_right = i
            else: # 거리가 같은 경우
                if hand == 'left':
                    answer += 'L'
                    cur_left = i
                else:
                    answer += 'R'
                    cur_right = i
                        
    
    return answer