# 할 일 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/181885

def solution(todo_list, finished):
    return [todo_list[i] for i in range(len(finished)) if not finished[i]]

# 다른 사람의 풀이
# zip 을 사용한 코드가 인상깊었습니다!