# 문자열 섞기
# https://school.programmers.co.kr/learn/courses/30/lessons/181942

def solution(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    
    answer = ''
    for a, b in zip(list1, list2):
        answer += (a + b)
    return answer