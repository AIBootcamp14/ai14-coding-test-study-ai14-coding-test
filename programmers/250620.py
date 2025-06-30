#%%
# 문제1 : 나머지 구하기
# 풀이
def solution(num1, num2):
    return num1 % num2

# 프로그래머스 다른 사람 풀이(맘에 든 풀이)
def solution(num1, num2):
    return divmod(num1, num2)[1]

# 다른 사람 풀이(신박한 풀이)
def solution(num1, num2):
    # return num1 % num2
    while num1 >= num2 :
        num1 -= num2
    return num1

#%%
# 문제2 : 머쓱이보다 키 큰 사람
# 풀이

#%% 
# 문제3 : 중앙값 구하기
# 풀이
