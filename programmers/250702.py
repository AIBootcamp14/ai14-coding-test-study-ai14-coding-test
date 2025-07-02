#%%
# 문제 1 : 정수 부분
# 풀이
def solution(flo):
    answer = int(flo)
    return answer
# 뭔가 이상한데.. 이게 맞나 싶은데 풀렸음.

# 프로그래머스 다른 사람 풀이_맘에 든 것
def soultion(flo):
    return flo//1

# 맘에 든 것2
import math
def solution(flo):
    answer = math.floor(flo)
    return answer

#%%
# 문제 2 : 가장 큰 수 찾기
# 풀이

#%%
# 문제 3 : rny_string
# 풀이
def solution(rny_string):
    if 'm' in rny_string:
        return rny_string.replace('m','rn')
    else:
        return rny_string

# 프로그래머스 다른 사람 풀이_맘에 든 것
# 비슷한 함수 쓰는데 이렇게 하면 더 간편
def solution(rny_string):
    return rny_string.replace('m','rn')
