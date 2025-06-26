# 1번 문제 : 덧셈식 출력하기

a, b = map(int, input().strip().split(' '))
print(f'{a} + {b} = {a + b}')

# 포맷팅하는 3가지 방법을 학습해 놓았으면 쉽게 풀 수 있다.
# 1. n = 10; print("%f" % n)
# 2. print("나는 {}시 {}분에 밥 먹을거야".format(7, 23)
# 3. time = 10; print(f'나는 오늘 집에 {time}에 갈거야')


# 2번 문제 : 숨어있는 숫자의 덧셈(1)
def solution(my_string):
    return sum([int(i) for i in my_string if i.isdigit()])
# list comprehension에 끝판왕 격 문제 for, if문을 동시에 한번에 사용
# 사용된 함수 sum, isdigit = 문자열이 숫자인지 아닌지를 boolean으로 반환해주는 함수


# 3번 문제 : 문자열을 정수로 변환하기
def solution(n_str):
    return int(n_str)

# 난이도 0

# [PCCP 기출문제] 1번 동영상 재생기
def solution(video_len, pos, op_start, op_end, commands):
    def change_time(string):
        string = string.split(':')
        time_value = int(string[0])*60 + int(string[1])
        return time_value

    def reverse_time(time_value):
        hour = time_value // 60
        sec = time_value % 60

        if hour < 10 :
            hour = '0' + str(hour)
        if sec < 10:
            sec = '0' + str(sec)
        return str(hour) + ':' + str(sec)

    video_len = change_time(video_len)
    pos = change_time(pos)
    op_start = change_time(op_start)
    op_end = change_time(op_end)

    if pos >= op_start and pos <= op_end: # initial status check!
            pos = op_end

    for command in commands:
        if command == 'next':
            pos = min(pos + 10, video_len)
        elif command == 'prev':
            pos = max(pos - 10, 0)
        if pos >= op_start and pos <= op_end:
            pos = op_end

    return reverse_time(pos)
# key point : 문자열로 이루어진 시간들의 비교를 위해 모두 초단위로 이루어진 정수형데이터로 변경한 후 비교
# key point 2 : 출력은 우리가 보는 시간과 똑같이 이루어져야 하니 다시 역으로 문자형 시간으로 출력하는 함수 생성
# key point 3 : 초기에 현재 시간도 opning term에 존재할 수 있으니 초기시간 확인!





