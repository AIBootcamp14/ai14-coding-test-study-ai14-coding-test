#%%   
# 문제 1 : 나이출력    
# 풀이
def solution(age) :
    answer = 2022 - age + 1 
    return answer

#%%
# 문제 2 : 모음제거
# 풀이(오답)
def solution(my_string): 
    drop_string = ('a','e','i','o','u')
    for i in drop_string
    answer = my_string.drop('i')
    return answer
# 틀린 이유 : 잘못된 함수 사용 -> 함수 기초 공부 필요

# chat GPT에 생각한 접근법 넣고 해결
# 생각한 접근법 : 모음을 담은 변수를 지정한 후 i가 변수에 포함되면, 그 변수는 제거한 문자열 출력
# drop_string = ('a','e','i','o','u')로 지정하고, for i in drop_string일 때 my_string.drop('i')로 출력하고 싶은데 오류 알려줘

# 문자열에는 .drop 메서드 없음
# 문자 'i'가 아닌 변수 i이기 때문에 따옴표 없이 작성
# 문자열에서 i를 ''(빈 문자열)로 바꿈(즉, 제거)
def solution(my_string) :
    replace_string = ('a','e','i','o','u')
    for i in replace_string:
        my_string = my_string.replace(i,'')
    return my_string

#%%
# 문제 3 : 삼각형의 완성조건
# 풀이(못 풀었음)
# if 문으로 조건을 넣어 구하면 되겠다 까지는 접근했으나, 어떻게 해야 할지 모르겠음
# chatGPT 도움 받음
# 숫자를 정렬해 가장 긴 변 찾기
def solution(sides) :
    sides.sort()
    return 1 if sides[2] < sides[0] + sides[1] else 2
