# 가장 큰 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/120899

def solution(array):
    sorted_list = sorted(array)
    num = sorted_list[-1]
    return [num, array.index(num)]

# 다른 사람의 풀이
# max() 함수 사용하여 최대값 구하기