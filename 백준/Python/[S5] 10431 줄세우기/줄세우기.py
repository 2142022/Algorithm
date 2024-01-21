from bisect import bisect_left
import sys
input = sys.stdin.readline

# 테스트케이스 수
P = int(input())
for _ in range(P):
    # 테스트케이스 번호, 아이들의 키
    T, *H = map(int, input().split())

    # 학생들이 뒤로 물러난 걸음 수의 총합
    cnt = 0

    # 최종 줄
    line = [H[0]]
    for i in range(1, 20):
        # 현재 아이의 키
        h = H[i]

        # 현재 아이가 들어갈 수 있는 위치
        idx = bisect_left(line, h)

        # 학생들이 뒤로 물어난 걸음 수
        if idx == 0:
            cnt += len(line)

        elif idx != len(line) - 1:
            cnt += len(line) - idx

        # 줄 서기
        line.insert(idx, h)

    print(T, cnt)