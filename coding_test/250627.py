# 25년 6월 27일(금)

# 1번 덧셈식 출력하기


# sol)
a, b = map(int, input().strip().split(' '))
print(f'{a} + {b} = {a + b}')



# key point
# input으로 a, b를 직접 입력 받기

# key point 2
# strip()로 입력 받은 숫자에 앞 뒤 공백 제거

# key point 3
# 입력 값으로 주어진게 "4 5"처럼 따로따로 입력하는 것이 아닌 한번에 공백을 넣어서 넣기 때문에
# 공백을 기점으로 숫자 a, b가 구분이 되기 때문에 split 함수를 통해 공백 기준으로 a, b를 나눈다.

# key point 4
# 포맷팅 세가지 방법.

# n = 10
# 1. print(f'{n}은 정수이다.') -> 10은 정수이다.
# 2. print('%d은 정수이다.' % n) -> 10은 정수이다.
# 3. print('{}은 정수이다.'.format(n)) -> 10은 정수이다.


##################################################################################################

# 2번 숨어있는 숫자의 덧셈 (1)

# sol)
def solution(my_string):
    return sum([int(i) for i in my_string if i.isdigit()])

# key point
# list comprehension : 리스트를 쉽게 짧게 한 줄로 만들 수 있는 파이썬의 문법으로 "파이써닉"하다는 표현의 핵심이 되는 문법
# 코드 가독성이 많이 높아지지만 길어지게 되면 되려 떨어지는 경우도 있어 적절히 사용하는게 필요하다.
# for문과 if문을 해당 문제처럼 섞어 쓸 수도 있다는 장점이 있다.



##################################################################################################

# 3번 문자열을 정수로 변환하기

# sol)
def solution(n_str):
    return int(n_str)





##################################################################################################

# 번외. 유연근무제

# sol)
def solution(schedules, timelogs, startday):
    gift_list = [True for i in schedules] # 지각한 사람 check하는 list
    # (startday - 1) % 7  >= 5 # 토일을 의미 하는 조건
    
    for ind, i in enumerate(timelogs):
        check_time = (schedules[ind] // 100) * 60 + schedules[ind] % 100 # 시간 단위를 분단위로 변환
        for ind2, j in enumerate(i):
            time = (j // 100) * 60 + j % 100 # 시간 단위 분단위로 변환
            if (startday - 1 + ind2) % 7 >= 5 :
                pass # 주말 예외처리!
            elif time - check_time > 10 :
                gift_list[ind] = False
    return sum(gift_list)

# keypoint 1.
# 시간 비교를 위해 시간단위를 통일해서 표현한다. 60분이되면 시간이 카운트가 올라가기 때문에 원활한 비교를 위해 모두 분 단위로 변환하는 부분이 필요

# keypoint 2.
# 예외되는 요일인 토일을 어떻게 if문을 통해 제외할 건지 고민 1일이 월요일이기 때문에 7에 나머지 계산을 통해 계산을 한다면 일요일 0, 토요일이 6이 되는데 이렇게 되면 수식처리가 가능은 하지만 번거로워 지기 때문에 1을 빼서 나머지의 값이 일요일 = 6, 토요일 = 5가 되게 조율한다.

# keypoint 3. 
# enumerate 함수를 쓰게 되면 list에 원소값 뿐만이 아닌 index까지 반환하게 되어 두개의 리스트를 전부 for문을 사용할 시 코드 구성을 원할하게 도움을 주는 함수이다. 

# keypoint 4.
# Breadth First Search 처럼 한번이라도 방문하게 되면 False 즉 해당 문제에서는 한번이라도 지각을 하게 되면 선물 자격을 잃게되는 걸 확인하는 list를 별도로 만들어 확인한다. 이렇게 하면 전부 제대로 출근했는지를 확인하는 것이 아닌 한번이라도 지각을 했는지를 확인하면 되서 좀 더 수월하게 문제를 풀 수 있다.






