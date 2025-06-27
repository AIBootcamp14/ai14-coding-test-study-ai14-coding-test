#%%
# Problem 1. Lv.0 덧셈식 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181947
# Solution 
a, b = map(int, input().strip().split(' '))
print(f'{a} + {b} = {a+b}')

#%%
# Problem 2. Lv.0 숨어있는 숫자의 덧셈 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120851
# Solution
def solution(my_string):
    answer = sum(map(int, list(filter(lambda x: x.isdigit(), list(my_string)))))
    return answer

#%%
# Problem 3. 문자열을 정수로 변환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181848
# Solution
def solution(n_str):
    return int(n_str)

#%%
# Problem 4. 문자열 압축하기
# https://school.programmers.co.kr/learn/courses/30/lessons/60057
# Solution

