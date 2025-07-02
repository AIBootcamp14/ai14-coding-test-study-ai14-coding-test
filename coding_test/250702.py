# 25.07.02(수)

# 1. 정수 부분

# sol)
solution = int

# keypoint 
# int함수를 통해 정수로 변환하면 소수부분이 버림된다는 특징을 이용


##############################################################################################


# 2. 가장 큰수 찾기

# sol)
def solution(array):
    answer = [-1 for i in range(2)]
    maxi = -1
    for ind, i in enumerate(array):
        if i > maxi :
            answer[0], answer[1] = i, ind
            maxi = i
    return answer

# keypoint
# 문제에 조건 중 array에 중복된 숫자가 없고 원소의 값은 0을 포함한 양의 정수 이기 때문에 최대값을 나타내는 maxi를 갱신하는 방식으로 진행
# maxi보다 큰 값을 찾게 되면 1). maxi를 update, 2). 답을 update
# enumerate라는 인덱스와 원소를 동시에 반환해주는 파이썬 내장함수를 잘 이용

# 고민한 것
# max함수를 통해 최대값을 찾고 해당 최대값의 인덱스를 찾아주는 find를 통해 문제를 풀려고 했으나 max함수 연산과 find함수 연산 모두 O(n)의 시간복잡도가 걸릴 것을 고려하여 효율성을 높이기 위해 한번 더 고민하게 됨 
# 중복된 원소가 없으므로 find말고 index를 쓰는 방법도 있음

##############################################################################################

# 3.rny_string

# sol)
def solution(rny_string):
    answer = ['rn' if i == 'm' else i for i in rny_string]
    return ''.join(answer)

# keypoint
# 일반적인 for문을 통해 조건을 걸어 answer를 더해나가면 쉽게 구할 수 있지만, list comprehension으로 작성하는 것이 Pythonic하므로 답안을 다음과 같이 작성을 하였다. 기존에 for문을 앞에 if문을 뒤에 걸어 조건에 맞는 원소만 리스트에 추가하는 방식이 아닌 if문을 앞에 for문을 뒤로 하여 조건에 맞는 원소를 변형하고 조건에 맞지 않은 원소를 그대로 리스트에 추가하는 방식으로 작성


##############################################################################################

# 번외. 문자열 압축

# 틀린풀이)
def solution(s):
    maxi_comp_num = len(s) // 2 # 최대 압축 수
    def comp_func(n):
        def inner_func(string):
            length = len(string)
            split_list = [string[i:i+n] for i in range(0, length, n)]

            result = []
            count = 1

            split_list_num = len(split_list)

            for i in range(split_list_num - 1):
                if (split_list[i] == split_list[i + 1]) :
                    count += 1
                elif (split_list[i] != split_list[i + 1]) and count > 1:
                    result += (str(count) + split_list[i])
                    count = 1
                else :
                    result += split_list[i]

                if i == split_list_num - 2 and count > 1:
                    result += (str(count) + split_list[i])
                elif i == split_list_num - 2 and count == 1:
                    result += split_list[i+1]
            return result
        return inner_func
    answer = []

    for i in range(1, maxi_comp_num + 1):
        comp = comp_func(i)
        result = comp(s)
        answer.append(len(result))
    return min(answer)

# sol) Gpt에 도움을 받은 풀이
def solution(s):
    if len(s) == 1:
        return 1

    max_len = len(s) // 2
    min_length = len(s)  # 압축하지 않은 원래 길이로 초기화

    for step in range(1, max_len + 1):
        compressed = []
        prev = s[0:step]
        count = 1

        for i in range(step, len(s), step):
            current = s[i:i+step]
            if current == prev:
                count += 1
            else:
                compressed.append(f"{count}{prev}" if count > 1 else prev)
                prev = current
                count = 1
        compressed.append(f"{count}{prev}" if count > 1 else prev)

        compressed_str = ''.join(compressed)
        min_length = min(min_length, len(compressed_str))

    return min_length


# keypoint
# 둘다 결과물은 같지만 나의 풀이는 closure구조를 이용해서 압축문자를 반환해주는 함수를 cutting 단위를 바꿀 때 재사용 할 수 있도록 코드를 구축하였다.
# 내 결과물의 시간효율성 문제로 한개의 test에서 통과를 하지 못하여 오답처리가 되었는데 주요 개선점으로는

# 1. closure를 통한 함수 재사용을 하던 함수를 단일 함수로 개선
# 2. 복잡한 인덱스 계산을 간단한 슬라이싱으로 처리
# 3. 마지막에 지속적으로 압축이 가능한 상황을 처리할때 마지막인덱스에 대한 조건 처리를 해주었는데 루프 탈출 후 일괄처리하는 것으로qusrud
# 4. 최종결과물로 반환하던 문자열을 + 연산을 통해 만들던 것을 join함수를 통해 개선

# 최종적으로
# 기존코드 : 복잡한 리스트 연산 + 마지막 인덱스 조건
# 개선 코드 : 문자열 슬라이싱 + 리스트 append + join

# 문자열 코드를 작성할 때 팁
# list에 필요 문자열을 입력하고 마지막에 join을 통한 압축이 가장 효율이 좋음

