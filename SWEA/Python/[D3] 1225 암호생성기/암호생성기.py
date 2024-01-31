from collections import deque

# 10개의 테스트케이스
for _ in range(10):
    # 테스트케이스 번호
    t = int(input())

    # 암호 데이터
    data = deque(map(int, input().split()))

    # 뺄 수
    m = 1

    # 앞에서부터 감소시킨 후, 맨 뒤로 보내기
    while not (max(data) < 10 and data[-1] == 0):
        data.append(max(0, data.popleft() - m))
        m += 1 if m < 5 else -4

    print(f'#{t} {" ".join(map(str, data))}')