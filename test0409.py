def solution(n, m):
    answer = []
    answer.append(0)
    # 삼항 연산자
    # 참일 경우 값 if 조건 else 거짓일 경우 값
    num = n if n > m else m
    for i in range(1, num + 1):
        if n % i == 0 and m % i == 0:
            answer[0] = i
    answer.append(n * m / answer[0])

    return answer