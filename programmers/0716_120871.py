# 저주의 숫자 3
# https://school.programmers.co.kr/learn/courses/30/lessons/120871

def solution(n):
    answer = 0
    cnt = 0
    while cnt < n:
        answer += 1
        if answer % 3 == 0:
            continue
        elif '3' in str(answer):
            continue

        cnt += 1
            
    return answer

# 방법이 딱히 떠오르지 않고 n 범위가 1<=n<=100이라고 해서 일단 while 반복
