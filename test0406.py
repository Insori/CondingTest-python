def solution(price, money, count):
    pay = 0
    for i in range(1, count+1):
        pay += (price*i)
    if(money < pay):
        return pay - money
    else:
        return 0

print(solution(3, 20, 4))