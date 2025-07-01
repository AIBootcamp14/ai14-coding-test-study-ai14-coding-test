# 25.07.01(화)

# 1. 특정한 문자를 대문자로 바꾸기

# sol)
def solution(my_string, alp):
    answer = ''
    my_string = my_string.lower()
    for i in my_string:
        if i == alp:
            answer += i.upper()
        else :
            answer += i

    return answer

# keypoint 
# lower로 초기화를 하고 조건문을 통해 문제에서 요구하는 조건을 구분해서 작성해준다.



##############################################################################################


# 2. 대문자와 소문자

# sol)
def solution(my_string):
    small_letter = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for i in my_string:
        if i in small_letter:
            answer += i.upper()
        else :
            answer += i.lower()
    return answer


# key point
# in 이라는 논리연산을 통해 소문자인지 대문자인지 구분하는 문자열을 생성 후 조건에 따른 결과물을 반환한다.
# 정규표현식을 이용하면 더욱 간결하게 문제를 해결할 수 있을듯

# 다른 풀이)


def solution(my_string):
    return my_string.swapcase()

# swapcase 라는 대소문자를 바꾸어주는 파이썬 내장함수가 이미 존재




# 또 다른 풀이)

def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else :
            answer += i.upper()
    return answer

# keypoint
# 대소문자인지 아닌지 불리언으로 반환해주는 함수를 이용 'abcd....z'를 통해 확인하는 문자열을 만들지 않아도 되서 더욱 간결함


##############################################################################################

# 3. 배열의 길이에 따른 다른 연산하기

# sol)
def solution(arr, n):
    length = len(arr)

    if length % 2 == 1: # 홀수 처리
        for i in range(0,length, 2):
            arr[i] = arr[i] + n
    else :              # 짝수 처리
        for i in range(1, length, 2):
            arr[i] = arr[i] + n

    return arr





##############################################################################################

# 번외. 완주하지 못한 선수 lv1 hash

# 효율성 테스트 실패답안)
def solution(participant, completion):
    for i in completion:
        participant.remove(i)
    return participant.pop()

# 틀린 답은 아니지만 remove하는 과정에서 시간복잡도가 매우 오래 걸려 효율성 측면에서 실패함.


# sol)

def solution(participant, completion):
    hash_list = {hash(i):i for i in participant}
    hash_total = 0
    for i in participant:
        hash_total += hash(i)
    for i in completion:
        hash_total -= hash(i)

    return hash_list[hash_total]

# keypoint 
# hash를 이용해 문자열을 특정 숫자로 변환하는 함수를 통해 선수이름을 구분함
# hash변환한 모든 선수의 이름을 hash_list라는 이름으로 dictionary를 만듬
# hash 변환하면 같은 이름을 가진 선수가 같은 hash number로 변환되기 때문에 for 문을 통해 총 합을 구하고, 다시 완주한 선수들의 hash num을 빼줘서 남은 hash num을 hash_list를 통해 변환한다면 매우 빠른 속도로 완주하지 못한 선수를 반환해 줄 수 있음


