def solution(s):
    answer = ''
    list = []
    for i in s:
        list.append(i)
    list.sort(reverse=True)
    for i in list:
        answer += i
    return answer

print(solution("Zbcdefg"))