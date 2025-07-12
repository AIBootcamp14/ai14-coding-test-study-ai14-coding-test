# 25.07.12(토)

# 1. 특정 문자 제거하기

# sol)
def solution(my_string, letter):
    answer = [i for i in my_string if i != letter]
    return ''.join(answer)

# keypoint 
# list comprehension


##############################################################################################


# 2. 접미사인지 확인하기

# sol)
def solution(my_string, is_suffix):
    length = len(my_string)
    answer = [my_string[i:] for i in range(length)]

    return int(is_suffix in answer)

# keypoint
# 모든 접미사를 구하기 위해 listcomprehension을 통해 구함
# 모든 접미사 리스트 안에 주어진 is_suffix가 포함되는지 유무를 반환


##############################################################################################

# 3. 접미사 배열

# sol)
def solution(my_string):
    answer = [my_string[i:] for i in range(len(my_string))]
    return sorted(answer)

# keypoint
# 모든 접미사를 listcomprehension을 통해 구한 후 sorted함수를 통해 정렬


##############################################################################################

# 4. 짝수는 싫어요

# sol)
def solution(n):
    answer = [i for i in range(1, n+1, 2)]
    return answer

# keypoint
# listcomprehension과 range 내장 함수의 추가 적인 옵션을 조합

##############################################################################################

# 5. 부분 문자열 이어 붙여 문자열 만들기

# sol)
def solution(my_strings, parts):
    answer = ''
    for part, st in zip(parts, my_strings):
        answer += st[part[0]:part[1] + 1]
    return answer

# keypoint
# zip 함수를 통한 my_strings, parts를 짝지어 한번에 호출
# 문자열에 인덱싱슬라이스에 대한 이해

##############################################################################################

# 6. 9로 나눈 나머지

# sol)
def solution(number):
    answer = 0
    for i in number:
        answer += int(i)
    return answer % 9

def solution(number):
    return int(answer)%9

# keypoint
# 문제에서 알려준 사실인 모든 자릿수를 더한 값을 9로 나눈 나머지도 원래 값을 9로 나눈 나머지와 같다는 사실을 이용
# 문자열에 그냥 list로 변환하면 한글자 단위로 원소가 되는 리스트로 반환됨
# 사실 그냥 9로 나눈 나머지 했어도 될듯 -> 되긴 되는데 위에 사용한 방식이 훨씬 빠름

##############################################################################################

# 7. 가위 바위 보

# sol)
def solution(rsp):
    answer = ''
    key_list = {'2': '0', '0':'5', '5':'2'}
    for i in rsp:
        answer += key_list[i]
    return answer

# keypoint
# 가위 바위 보를 냈을 때 이기는 것을 반환해주는 딕셔너리를 작성


##############################################################################################

# 8. 글자 이어 붙여 문자열 만들기

# sol)
def solution(my_string, index_list):
    answer = [my_string[i] for i in index_list]

    return ''.join(answer)

# keypoint
# for문을 통해 하나씩 이어 붙이는 방식보다 listcomprehension으로 일단 원하는 문자를 list형태로 만들어서 합쳐주는 것이 효율적
# 파이써닉한 코드작성법


##############################################################################################

# 9. 수 조작하기 2

# sol)
def solution(numLog):
    answer = ''
    for i in range(len(numLog) - 1):
        temp = numLog[i + 1] - numLog[i]
        if temp > 0:
            if temp == 1:
                answer += 'w'
            else :
                answer += 'd'
        else :
            if temp == -1:
                answer += 's'
            else :
                answer += 'a'
    return answer

# keypoint
# 문제에서 주어진 조건을 구현


# 또 다른 풀이
def solution(log):
    res=''
    joystick=dict(zip([1,-1,10,-10],['w','s','d','a']))
    for i in range(1,len(log)):
        res+=joystick[log[i]-log[i-1]]
    return res

# 조건에 해당하는 부분을 딕셔너리 답지를 만들어 놓아서 호출하는 방식으로 진행
