# 25.07.10(목)

# 1. 공용문제 1: 옹알이(1)

# sol)
def solution(babbling):
    answer = 0
    key_list = ['aya', 'ye', 'woo', 'ma']
    for i in babbling:
        for j in key_list:
            i = i.replace(j, '/')
        i = i.replace('/', '')
        if not i :
            answer += 1

    return answer

# keypoint 
# babbling 원소 하나 당 발음 할 수 있는 발음 최대 한개까지만 나오기 때문에 모든 발음 가능한 단어를 순회해서 replace로 대체
# 그냥 blink로 대체하게 되면 압축되어서 예외되는 사항이 발생하기 때문에 이를 주의하여 아무 문자 (알파벳이 아닌 문자)로 바꾸어 마지막에 해당 문자를 blink로 변환하여 체크


##############################################################################################


# 2. 공용문제 2: 3진법 뒤집기

# sol)
def solution(n):
    answer = 0

    result = '' # 3진수 변환된 값을 저장한 객체
    # 3진수 변환
    while n > 2:
        result += str(n % 3)
        n //= 3
    result += str(n)

    result =str(int(result)) # 0을 없애는 과정

    for ind, i in enumerate(result[::-1]): # 뒤에서 붙어 호출
        answer += int(i) * (3**ind)

    return answer

# keypoint
# 3진법으로 어떻게 변환하는지를 고민
# 3진법 변환을 언제 멈추어야하는지 조건 생각
# 숫자로된 문자열을 숫자형으로 변환하면 어떻게 되는지 생각
# 3진법을 어떻게 10진법으로 바꿀지 고민
# 뒤에서 부터 호출하는 방법 


##############################################################################################

# 3. 가장 큰 수

# sol)
def solution(numbers):
    def iter_func(num):
        length = len(num)
        if length == 1:
            return num*4
        elif length == 2:
            return num*2
        elif length == 3:
            return num + num[0]
        else :
            return num


    numbers = [str(i) for i in numbers]
    numbers.sort(key = lambda x : iter_func(x), reverse = True)
    return str(int(''.join(numbers)))

# keypoint
# 문자열 숫자는 어떻게 정렬하는지 이해해야한다.
# 문자열 숫자는 첫째 자리를 우선 비교를 하고 첫째자리가 같으면 다음 자리수를 비교하는데 다음 자리수가 없으면 제일 먼저 정렬되고 그다음 두번째 자리를 비교하는 순으로 정렬된다 즉 인덱스 0번부터 비교하면서 정렬하고 0번째가 같으면 다음번째를 비교하는데 존재하지 않으면 내려감

# 이와 같은 성질을 이용해 큰 자릿수와 작은 자릿수의 첫번재자리가 같다면 작은 자릿수를 전부 읽으면서 비교하고 작은 자릿수 전부를 비교했다면 작은 자릿수는 다시 0번째 인덱스에 있는 것을 가지고 비교를 하게 된다.
# 따라서 별도의 기준이 되는 함수 전부 반복해서 4자리수를 만드는 함수를 만들어 정렬 하게되면 문제 해결
