#%%
# 문제1 : 문자열 돌리기
# 풀이

#%%
# 문제 2 : 문자열 정렬하기(1)
# 풀이

#%% 
# 문제3 : 부분 문자열인지 확인하기
# 풀이
def solution(my_string, target):
    if target in my_string:
        return 1
    else:
        return 0
# 이 풀이로 했는데, 하나는 null 값이 나와서 아래 풀이로 했더니 됐음
# 근데 이게 맞는 풀이인가 싶고...
def solution(my_string, target):
    if target in my_string:
        return 1
    elif target not in my_string:
        return 0

# 프로그래머스 다른 사람 풀
# 처음에 했던 풀이랑 비슷하게 했는데 나는 왜 안 됐을까?
def solution(my_string, target):
    return 1 if target in my_string else 0
