#%%
# Problem 1. Lv.0 대문자로 바꾸기
# https://school.programmers.co.kr/learn/courses/30/lessons/181877
# Solution
def solution(myString):
    return myString.upper()


#%%
# Problem 2. Lv.0 배열의 길이를 2의 거듭제곱으로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181857
# Solution
def solution(arr):
    for k in range(11):
        if len(arr) == 2**k:
            return arr
        elif 2**k < len(arr) < 2**(k+1):
            return arr + [0] * (2**(k+1) - len(arr))
        

#%%
# Problem 3. Lv.0 배열 조각하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181893
# Solution
def solution(arr, query):
    for i, v in enumerate(query):
        if i%2 == 0:
            arr = arr[:v+1]
        else:
            arr = arr[v:]
    return arr


#%%
# Problem 4. Lv.2 모음사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512
# Solution

