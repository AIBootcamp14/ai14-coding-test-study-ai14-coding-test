# 첫 번째로 나오는 음수
# https://school.programmers.co.kr/learn/courses/30/lessons/181896

def solution(num_list):
    filtered = [i for i in range(len(num_list)) if num_list[i] < 0]
    if filtered:
        return filtered[0]
    else:
        return -1