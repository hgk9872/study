# https://school.programmers.co.kr/learn/courses/30/lessons/92334
# 딕셔너리를 잘 다루기...

##### 알아둘것 리스트 ######
# for key, value in dict.items():

#### 딕셔너리 컴프리헨션
# dict2 = {x: 0 for x in keys}

#### 딕셔너리에서 key로 value 뽑기
# dict[key] => value

#### 리스트에서 index함수 쓰는법
# a_list = ['ho', 1, 7]
# a_list.index(7)           // 2 출력
# a_list.index('ho')        // 0 출력


def solution(id_list, report, k):
    # id_list : 이용자의 아이디
    # report : "이용자id 신고한id"
    # 유저가 정지되면, 해당 유저를 신고한 모든 유저에게 정지메일 보냄
    # id_list에서, 자기가 신고한 유저가 개수만큼 리턴
    
    # report 중복 제거
    report = set(report)
    
    # 신고자 횟수 저장 dictionary
    report_dict = {id: 0 for id in id_list}
    for x in report:
        report_dict[x.split()[1]] += 1
    
    answer = [0] * len(id_list)
    
    # 정지먹은 사람만...
    for x in report:
        if report_dict[x.split()[1]] >= k:
            answer[id_list.index(x.split()[0])] += 1

    return answer