#%%
# 문제1 : 덧셈식 출력하기
# 풀이
a, b = map(int, input().strip().split(' '))
print(f'{a + b =}', a+b)
# 위 식으로 해결하려 했으나, 말 그대로 a + b = a+b값 a+b값이 나와서 한참 고민하다 일단은 풀었음

a, b = map(int, input().strip().split(' '))
print(str(a), '+', str(b), '=', a+b)
# 뭔가 지저분해진 느낌이 들음

# 프로그래머스 다른 사람 풀이(내가 하고 싶었던 것)
a, b = map(int, input().strip().split(' '))
print(f"{a} + {b} = {a + b}")
# 이쯤되면 머릿속에 지우개 있는 것 같음.. 언제까지 기초만 할 거냐고...

#%%
# 문제2 : 숨어있는 숫자의 덧셈(1)
# 풀이

#%%
# 문제3 : 문자열을 정수로 변환하기
# 풀이
def solution(n_str):
    answer = int(n_str)
    return answer
