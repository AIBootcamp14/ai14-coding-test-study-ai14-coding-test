# ad 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181870

def solution(strArr):
    return [str for str in strArr if "ad" not in str]