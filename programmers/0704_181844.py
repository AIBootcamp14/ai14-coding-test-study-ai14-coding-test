# 배열의 원소 삭제하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181844

def solution(arr, delete_list):
    return [item for item in arr if item not in delete_list]