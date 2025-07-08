#이상한 문자 만들기 (school.programmers.co.kr/learn/courses/30/lessons/12930)

def weird(s):
    string = s.split(" ")
    weird_string = []
    for word in string:
        word = word.lower()
        for i in range(len(word)):
            if i % 2 == 0:
                word = word[:i] + word[i].upper() + word[i+1:]
            else:
                pass
        weird_string.append(word)
    return ' '.join(weird_string)

weird("try hello world")

#Takeaway: 애초에 다 소문자로 변환하면, 대문자만 처리해야 하여 간결해짐