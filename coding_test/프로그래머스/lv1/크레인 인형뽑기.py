# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    
    answer = 0
    result = [] # 바구니
    
    prev_item = 0 # 이전에 바구니에 들어갔던 아이템
    
    # 순서대로 좌우로 움직임
    for move in moves:
        # 위에서부터 아래로
        for i in board:
            if i[move-1] != 0: # 해당 번호 위치에서 인형이 있다면
                now_item = i[move-1] # 현재 아이템
                if len(result) > 0:
                    prev_item = result[-1] # 바구니에 위에 있는 아이템
                    if now_item == prev_item: # 두 아이템이 같다면
                        result.pop()
                        answer += 2
                    else:
                        result.append(now_item) # 바구니에 넣고
                else:
                    result.append(now_item)
                i[move-1] = 0 # 뽑은 아이템에 대해 리스트에서 비운다
                break
                
    return answer