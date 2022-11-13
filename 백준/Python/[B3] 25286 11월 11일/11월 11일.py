import datetime

# 테스트케이스 개수
T = int(input())

# T개의 테스트케이스
for i in range(T):

    # 년도와 월 입력받기
    year, month = map(int, input().split())

    # 결과: 입력받은 년도, 월, 1일의 하루 전날
    date = datetime.date(year, month, 1) + datetime.timedelta(days=-1)

    print(date.year, date.month, date.day)