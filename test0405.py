def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        answer = True
        for i in s:
            if i < chr(48) or i > chr(57):
                answer = False
                break
    else:
        answer = False
    return answer


print(solution("a234"))
print(solution("1234"))
