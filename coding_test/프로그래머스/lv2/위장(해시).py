# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    # 최소 한개는 입는다
    
    # type_set = set()
    
    # # 옷 종류 집합
    # for row in clothes:
    #     type_set.add(row[1])
    
    clothes_dict = {}
    
    answer = 1
    
    for row in clothes:
        if row[1] in clothes_dict.keys():
            clothes_dict[row[1]].append(row[0])
        else:
            clothes_dict[row[1]] = [row[0]]
    
    for x in clothes_dict.values():
        answer *= (len(x) + 1)
    
    return answer - 1