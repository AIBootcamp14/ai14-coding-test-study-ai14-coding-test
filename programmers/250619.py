#%%
# 문제1 : 문자 반복 출력하기
# 풀이

#%%
# 문제2 : 순서쌍의 개수
# 풀이

#%%
# 문제3 : 중복된 숫자 개수
# 풀이
def solution(array, n):
    for i in array:
        return array.count(n)

# 프로그래머스 다른 사람 풀이(내 기준 베스트)
def solution(array, n):
    return array.count(n)

# 같은 for문 다른 풀이 방식
def solution(array, n):
    answer = 0
    for i in range(len(array)):
        if array[i] == n :
            answer += 1
    return answer
