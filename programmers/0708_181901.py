# 배열 만들기 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181901

def solution(n, k):
    return [i for i in range(1, n+1) if i % k == 0]

# 다른 사람의 풀이
# range(start, end, step) 사용에 익숙해져야 할 것 같다는 생각이 들었습니다.