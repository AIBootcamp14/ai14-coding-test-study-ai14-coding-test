# 3진법 뒤집기
# https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    ternary_str_list = list(get_ternary_number_str(n))
    ternary_str_list.reverse()
    reversed_str = "".join(s for s in ternary_str_list)
    return get_ternary_to_decimal(reversed_str)

# 10진법수를 3진법수 문자열로 반환
def get_ternary_number_str(number):
    tmp = number
    result = ''
    while tmp / 3 != 0 or tmp % 3 != 0:
        m = int(tmp / 3)
        n = int(tmp % 3)
        result = str(n) + result
        tmp = m
    if tmp != 0:
        result = str(tmp) + result
    return result

# 3진법수 문자열을 10진법 int로 반환
def get_ternary_to_decimal(num_str):
    num_list = list(num_str)
    result = 0
    for i in range(len(num_list)):
        tmp = (3 ** (len(num_list)-i-1) ) * int(num_list[i])
        result += tmp
    return result

# 다른 사람의 풀이
#     tmp = ''
#     while n:
#         tmp += str(n % 3)
#         n = n // 3
#     answer = int(tmp, 3)
# 간단하게 줄일만한 방법을 찾지 못해 하나하나 코딩 ㅠㅠ
# //, %를 적절하게 사용하는 방법 공부해보기