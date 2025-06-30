#%%
# 문제1 : 카운트 업
# 풀이

#%%
# 문제2 : 옷가게 할인 받기
# 풀이
def solution(price):
    i = price * 0.8
    j = price * 0.9
    h = price * 0.95
    if price >= 500000:
        i
    elif price >= 300000:
        j
    else price >= 100000:
        h
    return
# 처음엔 이렇게 적어놓고 return에 무엇을 적어야 하는지 한 시간을 고민해도 답이 안 나와서
# 너무 풀고 싶어서 지피티 선생님께 힌트를 얻었음

# <조건문에 결과를 출력해야 한다>는 힌트를 얻고 아래와 같이 고쳤음
def solution(price):
    if price >= 500000:
        return price * 0.8
    elif price >= 300000:
        return price * 0.9
    else price >= 100000:
        return price * 0.95
    return price

# 제한 사항인 정수 출력과 10만 원 이하 구매 조건을 안 적어서 아래와 같이 고침
def solution(price):
    if price >= 500000:
        return int(price * 0.8)
    elif price >= 300000:
        return int(price * 0.9)
    elif price >= 100000:
        return int(price * 0.95)
    else:
        return price

# 프로그래머스 다른 사람 풀이(생각하지 못한 풀이법)
def solution(price):
    discount_rates = {500000:0.8, 300000:0.9, 100000:0.95, 0:1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)

#%%
# 문제3 : 부분 문자열
# 풀이
def solution(str1, str2):
    return 1 if str1 in str1 else 0
