# 이상한 문자 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    index = 0
    answer = ''
    for c in s:
        if c == ' ': # 공백인 경우 다음 문자부터 다시 대문자
            index = 0
            answer += c
            continue
        else:
            if index % 2 == 0:
                answer += c.upper()
            else:
                answer += c.lower()
        index += 1
    return answer