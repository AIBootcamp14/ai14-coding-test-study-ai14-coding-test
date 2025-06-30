# 25년 6월 30일 (월)


# 1. A강조하기

# sol)

def solution(myString):
    answer = ''
    
    myString = myString.lower() # 초기화
    
    for i in myString:
        if i == 'a':
            answer += 'A'
        else :
            answer += i
    
    return answer

# keypoint 1. 
# 처음에 주어진 문자열을 lower함수를 통해 초기화하는 과정을 거친다면 쉽게 해결이 가능하다.

##########################################################################################



# 2. 암호해독

# sol)

def solution(cipher, code):
    code_list = [i for ind, i in enumerate(cipher) if (ind + 1) % code == 0]
    
    return ''.join(code_list)

# keypoint 1.
# list comprehension 문법을 통해 문제에서 주어진 조건에 맞는 문자열만 뽑아서 리스트로 만들기


# keypoint 2. 
# 조건의 맞는 문자열을 합치기 위한 join함수를 사용한다. 'a'.join(list) -> 리스트에 있는 원소를 a를 사이에 껴서 합쳐준다.




##########################################################################################



# 3. 뒤에서 5등 위로

# sol)
def solution(num_list):
    num_list.sort()
    return num_list[5:]


# key point.
# 개인적으로 파이썬에서 제공하는 sort는 배웠던 sort중에 무엇인지 궁금해서 검색해 보니 Timsort = Merge sort Insertion sort를 결합한 하이브리드 정렬 알고리즘을 사용하고 있으면 개발자는 Tim Peters이며, 개발자의 이름을 딴 Timsort라고 부르고 있다.

# 해당 sort 방법에 시간 복잡도 최악 : O(n log n), 최선 : O(n) 매우빠르고 다양한 상황에서 매우 효율적인 것으로 잘 알려져있다. 

