# 25.07.08(화)

# 1. 세균 증식

# sol)
def solution(n, t):
    return n * (2 ** t)
# keypoint 
# 간단한 수식 계산 승수 계산 연산자를 잘 생각하면됨 



##############################################################################################


# 2.배열에서 문자열 대소문자 변환하기

# sol)
def solution(strArr):
    return [i.lower() if ind % 2 == 0 else i.upper() for ind, i in enumerate(strArr)]

# keypoint
# list comprehension


##############################################################################################

# 3. 첫 번째로 나오는 음수

# sol)
def solution(num_list):
    iter_num = iter(num_list)
    try :
        count = 0
        while iter_num:
            if next(iter_num) < 0 :
                return count
            count += 1
    except :
        return -1

# keypoint
# iter 함수를 통해 iterator를 만들어 준다. 모든 리스트를 전부 다 훑으면서 작업하는 것보다 하나씩 호출하는게 효과적임
# 전부다 호출했는데도 반복문이 실행이 되면 정상적으로 실행이 되는 것이 아닌 오류코드가 반환되기 때문에 try except구문으로 처리 오류코드가 발생하면 음수가 없다는 의미이기 때문에 -1 반환 


##############################################################################################

# 4. 문자열의 앞의 n글자

# sol) 
def solution(my_string, n):
    return my_string[:n]

# keypoint
# 기초 슬라이싱



##############################################################################################

# 5. 할 일 목록

# sol)
def solution(todo_list, finished):
    answer = []
    for fini, todo in zip(finished, todo_list):
        if not fini:
            answer.append(todo)
        
    return answer

# keypoint
# zip 함수를 통해 pair하게 반복문의 사용할 인자를 받아 올 수 있음




##############################################################################################

# 6. 배열 만들기 1

# sol)
def solution(n, k):
    return list(range(k,n + 1,k))

# keypoint
# 내장함수 range를 이용한 간단한 해결



##############################################################################################

# 번외. 피보나치 수

# sol)
def solution(n):
    if n == 0 : 
        return 0
    elif n <= 2:
        return 1
    
    prev = 1 # fibo 2
    current = 2 # fibo 3
    for i in range(4,n + 1):
        prev, current = current, current + prev
        
        #temp = current
        #current = current + prev # update current
        #prev = temp # update prev    # 위의 처럼 동시할당 구문을 작성하지 않으면 current를 임시로 받을 객체가 필요로 해짐

    return current % 1234567

# 다이나믹 프로그래밍과 관련된 문제
# 간단히 해결하기 위해 재귀함수를 이용하여 fibonacci를 구현하면 후입선출 구조로서 매우 시간복잡도가 커지는 문제가 발생
# 이를 해결하기 위해 이전 시점에 fibonacci를 기억하고 prev, 현재 시점의 fibonacci를 갱신 current
# 기본 아이디어는 이렇지만 동시 할당이 가능한 파이썬에서 간단하게 작성가능
# 동시 할당이아니면 임시 저장을 하는 객체를 따로 받아서 구조가 복잡해짐



