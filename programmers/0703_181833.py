# 특별한 이차원 배열 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181833

def solution(n):
    answer = []
    for i in range(n):
        arr = []
        for j in range(n):
            if i == j:
                arr.append(1)
            else:
                arr.append(0)
        answer.append(arr)
    return answer

# 다른 사람의 풀이
# for 문을 한번만 사용하여
# 한 행의 배열을 먼저 생성 후
# index i 값을 1로 바꿔주는 코드가 인상깊었습니다.