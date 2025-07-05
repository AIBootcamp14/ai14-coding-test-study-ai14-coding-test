# 25.07.04(금)

# 1. 주사위 게임 1

# sol)
def solution(a, b):
    result = sum([a % 2 == 1, b% 2 == 1])
    if result == 2 :
        return a**2 + b**2
    elif result == 1 :
        return 2*(a + b)
    else :
        return abs(a - b)

# keypoint 
# 둘 중 하나만 홀수라는 조건식을 세우기 번거롭기 때문에 더해서 1인 것을 활용해서 조건 식을 완화


##############################################################################################


# 2. 배열의 원소 삭제하기

# sol)
def solution(arr, delete_list):
    for i in delete_list:
        if i in arr:
            arr.remove(i)
    return arr

# keypoint
# arr안에 delete 원소가 있는지 확인을 하지 않으면 모든 delete원소에 대해 remove를 하기 때문에 효율적이지 못함 remove가 in을 통한 논리연산을 계산하는 것보다 더 많은 시간이 소요되기 때문


##############################################################################################

# 3. ad 제거하기

# sol)
def solution(strArr):
    answer = []
    for i in strArr:
        if 'ad' in i:
            pass
        else :
            answer.append(i)
    return answer

# keypoint
# 문자열의 데이터 타입의 특성을 잘 파악하고 있는지 확인하는 문제로서 좋은 듯
# 문제에서 말한 'ad'가 str array에 포함되고 있는지 여부는 in 논리연산자로 쉽게 확인이 가능하다. for문을 돌렸을 때 string array면 idx순으로 원소의 해당하는 string이 호출되고 array가 아닌 string이 for문으로 호출한다면 string 한글자 한글자가 list처럼 호출되는 것을 잘 인지해야한다.


##############################################################################################

# 번외. 교점에 별 만들기

# 오답
def solution(line):
    coord = []
    answer = []
    for i in range(len(line) - 1):
        for j in range(i+1, len(line)):
            A, B, E = line[i]
            C, D, F = line[j]
            if (A*D - B*C) == 0 :
                pass
            else : 
                x = (B*F - E*D)/(A*D - B*C)
                y = (E*C - A*F)/(A*D - B*C)
                if x == int(x) and y == int(y):
                    coord.append([int(x), -int(y)])
    col1, col2 = zip(*coord)
    x_min, y_min = min(col1), min(col2)
    coord = [[row[0] - x_min, row[1] - y_min] for row in coord]
    
    col1, col2 = zip(*coord)
    x_max, y_max = max(col1), max(col2)
    
    coord = sorted(coord, key = lambda x : (x[1], x[0]))
    print(coord)
    for j in range(y_max + 1):
        temp = ''
        for i in range(x_max + 1):
            coord_x, coord_y = coord[0]
            if i == coord_x and j == coord_y :
                temp += '*'
                del coord[0]
            else : 
                temp += '.'
        answer.append(temp)
  
    return answer
# 통과가 일부 되지만 실행시간이랑 모든 케이스를 커버하지 못함...
# 고려 할 것이 매우 많은 문제


# sol)
def solution(line):
    coord = []
    answer = []
    for i in range(len(line) - 1):
        for j in range(i+1, len(line)):
            A, B, E = line[i]
            C, D, F = line[j]
            if (A*D - B*C) == 0 :
                pass
            else :
                x = (B*F - E*D)/(A*D - B*C)
                y = (E*C - A*F)/(A*D - B*C)
                if x == int(x) and y == int(y):
                    coord.append([int(x), -int(y)])
    col1, col2 = zip(*coord)
    x_min, y_min = min(col1), min(col2)
    coord = [[row[0] - x_min, row[1] - y_min] for row in coord]

    col1, col2 = zip(*coord)
    x_max, y_max = max(col1), max(col2)

    grid = [['.']*(x_max + 1) for _ in range(y_max + 1)]

    for x, y in coord :
        grid[y][x] = '*'
    return [''.join(grid[i]) for i in range(len(grid))]

# keypoint
# 위 오답에서는 빈 좌표를 만들 때 1차원 즉 대괄호를 하나를 쓰는 방식으로 만들어 인덱스를 두개를 써 넣어 해당 인덱스에 좌표를 기입해 *로 바꾸는 방식을 사용하였지만 인덱스 두개를 부여하려면 반드시 2차원 리스트를 이용해야한다.
# 문자열을 for문의 입력값으로 불러오면 list형식처럼 문자 하나하나 호출이 되기 때문에 리스트처럼 느낄 수 있으나 이는 list가 아니므로 'aaaa'에 세번째 a를 b로 바꾸기 위해 s = 'aaaa'; s[2] = 'b'를 입력하면 바뀌지 않고 바꾸길 원한다면 새로이 문자열을 만들어 s = s[:2] + 'b' + s[3:] 처럼 기입해야 원하는 바가 실행된다.

# 이와 같은 문자열에 특성을 고려하여 2차원 배열안에 원소하나하나를 ['.']으로 채워놓고 해당하는 원소의 문자열을 ['*'] 바꾸어 다시 문제에서 원하는 출력 형식이 1차원 리스트로 반환한다.


# zip 함수는 주어진 리스트를 짝지어주는 역할을 한다 주의점은 무조건 짧은 리스트에 맞추어 반환해준다.

# *data는 언패킹 연산자이다 [[1, 2], [3, 4]]처럼 대괄호가 2개 쓰여진 2차원 리스트를 대괄호 한개인 [1, 2], [3, 4]로 반환해주는 연산이다.

# zip(*data)를 입력하게 되면 언패킹 후 리스트 끼리 묶어주는 함수를 적용해 튜플로 반환하는 작업을 하게되는 것이다 즉, (1,3), (2,4)로 반환 

# 2차원을 입력하게 되면 행 단위로 묶여있던 list가 열단위로 묶을 수 있는 듯 다양한 작업들을 할 수 있음 
