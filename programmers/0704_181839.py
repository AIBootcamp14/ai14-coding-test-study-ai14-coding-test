# 주사위 게임 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181839

def solution(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return abs(a-b)
    elif a % 2 != 0 and b % 2 != 0:
        return a*a+b*b
    else:
        return 2*(a+b)

# 다른 사람의 풀이
# 비트 연산자로 짝수, 홀수를 구분하고 *2 를 << 1 을 통해 연산한게 인상깊었습니다.
