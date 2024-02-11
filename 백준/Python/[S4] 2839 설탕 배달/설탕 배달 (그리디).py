N = int(input())

# 5킬로그램 봉지로 나눠지면 바로 출력
if N % 5 == 0:
    print(N//5)
    
else:
    # 3킬로그램 봉지의 개수
    num = 0

    # 5킬로그램 봉지 수를 하나씩 줄여가면서 N킬로그램 맟추기
    for i in range(N//5, -1, -1):

        # 남은 무게가 3으로 나워지면 봉지수 출력
        if (N - 5 * i) % 3 == 0:
            print(i + (N - 5 * i) // 3)
            num += 1
            break

    # 정확하게 N킬로그램을 만들 수 없는 경
    if num == 0:
        print(-1)
