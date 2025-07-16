# 옹알이 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120956

def solution(babbling):
    speakable = ["aya", "ye", "woo", "ma"]
    answer = 0

    for word in babbling:
        tmp = word
        for s in speakable:
            cnt = 0
            if s in tmp: 
                # babling 단어 중 발음할 수 있는 단어를 찾으면
                # 처음 일치한 문자열만 공백으로 replace
                # 제거되었을 때 다른 문자와 붙어서 발음할 수 있는 단어로 체크되는 것 방지
                tmp = tmp.replace(s, ' ', 1) 
                cnt += 1

            if len(tmp.strip()) == 0:
                answer += cnt

    return answer

# 다른사람의 풀이
# regex = re.compile('^(aya|ye|woo|ma)+$')
# 정규표현식 좀 공부해야겠다고 생각했습니다.