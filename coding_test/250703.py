# 25.07.03(목)

# 1. 특이한 이차원 배열 1

# sol)
def solution(n):
    answer = [[0] * n for _ in range(n)]
    for i in range(n):
        answer[i][i] = 1
    return answer

# keypoint 
# 일명 Identity matrix 항등행렬이라고 하는 행렬을 만들고자 하는 것이 문제이다
# [0] 부분을 for문을 통해 한번 더 조건문을 더욱 간결하게 한 줄로 문제를 풀 수 있지만 시간복잡도가 O(n^2)으로 증가하게 된다. 조금더 많이 코드를 작성하게 되지만 위 풀이처럼 하는 것이 시간 복잡도O(2n)으로 훨씬 빠른 속도로 실행이 된다.

# 즉 간결한 코드가 무조건 좋은 것은 아님


##############################################################################################


# 2. 0 떼기

# sol)
def solution(n_str):
    prev = n_str[0]

    if prev == '0' :
        idx = 1
        current = n_str[idx]
        while prev == current:
            idx += 1
            current = n_str[idx]
    else :
        return n_str

    return n_str[idx:]

# keypoint
# 앞에서 부터 0인지 아닌지를 확인하는 코드를 작성
# 처음부터 0이 아닌경우 바로 출력
# 0인 경우 다음 숫자와 비교해서 똑같이 0인 경우 반복
# 문제에서 0으로만 이루어진 경우가 없어서 다음과 같이 작성하였지만, 0으로만 이루어진 경우가 있는경우 while문에 idx가 input str보다 커진경우 중지하는 조건문을 처리해준다


##############################################################################################

# 3. 공백으로 구분하기 2

# sol)
def solution(my_string):

    prev = my_string[0]
    answer = []
    if prev.isalpha():
        temp = prev
    else:
        temp = ''
    for i in range(1,len(my_string)):
        current = my_string[i]
        if current.isalpha() and prev.isalpha():
            temp += current
            prev = current
        elif current.isalpha() and not prev.isalpha():
            temp += current
            prev = current
        elif not current.isalpha() and prev.isalpha():
            answer.append(temp)
            temp = ''
            prev = current
        else :
            prev = current
    if temp : answer.append(temp)
    return answer

# keypoint
# 생각보다 어려웠던 문제, strip으로 앞뒤 공백 없애고 replace, split 등의 내장 함수를 이용하면 쉽게 해결이 될 줄 알았지만 공백이 여러번 반복하는 경우 때문에 생각보다 어려웠음
# 따라서 현재와 과거를 나타내는 객체를 정해 prev, current를 가지고 지속적인 비교를 통해 모든 조건 행동을 걸어준다
# 마지막 까지 공백이 아닌 문장인 경우 temp가 답안에 저장되지 않으므로 temp가 공백이 아닌경우 answer에 추가하는 조건을 for문을 벗어나서 처리해준다.



##############################################################################################

# 번외. 공통문제 이상한 문자 만들기

# 오답)
def solution(s):
    answer = ''
    for ind, i in enumerate(s):
        if ind % 2 == 0:
            answer += i.upper()
        else :
            answer += i.lower()

# 문제를 정확하게 파악하지 못하고 단순히 짝수번째는 대문자 홀수번째는 소문자로 변환하는 방식인줄 알았음


# sol) 
def solution(s):
    answer = []
    s_list = s.split(' ')
    for i in s_list:
        temp = ''
        for ind, j in enumerate(i):
            if ind % 2 == 0:
                temp += j.upper()
            else :
                temp += j.lower()
        answer.append(temp)

    return ' '.join(answer)

# keypoint
# 문장마다 홀수 번째 소문자,  짝수 번째 대문자 적용을 시켜야 하므로 문장 단위로 list로 저장
# 해당 문장 마다 for문을 돌리는 for문안에 for문 방식으로 실행

# list를 다시 원래 형태의 문장을 만들기 위해 ' '.join을 사용해서 output만들어줌




