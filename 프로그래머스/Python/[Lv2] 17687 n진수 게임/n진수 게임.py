# https://school.programmers.co.kr/learn/courses/30/lessons/17687

# number를 n진법으로 바꾸기
def getNum(number, n):
    result = []
    
    while number >= n:
        result.append(number % n)
        number //= n
    
    result.append(number)
    
    # 10 이상인 수는 알파벳으로 변환, 나머지는 string으로 변환
    b = ['A', 'B', 'C', 'D', 'E', 'F']
    for i in range(len(result)):
        if result[i] >= 10:
            result[i] = b[result[i] - 10]
        else:
            result[i] = str(result[i])

    # 현재 구한 리스트의 순서를 거꾸로
    result.reverse()
    
    return result
    
##############################################################

# n: n진법
# t: 미리 구할 숫자의 개수
# m: 게임에 참가하는 인원
# p: 튜브의 순서
def solution(n, t, m, p):
    # 튜브가 말해야 하는 t개의 숫자
    result = []
    
    # t개의 숫자를 구하기 위해서는 총 m X t개의 숫자를 구해야 함
    # m X t개의 숫자
    total = []
    
    # 0부터 n진법으로 바꾸기
    number = 0
    
    while len(total) <= m * t:
        total += getNum(number, n)
        number += 1
    
    # 인덱스 % (참가 인원 수) == (튜브의 순서 - 1) 인 숫자 구하기
    for i in range(len(total)):
        if i % m == p - 1:
            result.append(total[i])
            
            # result의 원소의 개수가 t개가 되면 끝내기
            if len(result) == t:
                break

    answer = ''.join(result)
    return answer
