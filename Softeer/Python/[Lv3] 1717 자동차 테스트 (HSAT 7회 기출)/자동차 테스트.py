from bisect import bisect_left
import sys
input = sys.stdin.readline

# n: 자동차 수, q: 질의 수
n, q = map(int, input().split())

# n개의 자동차의 연비
cars = list(map(int, input().split()))
# 오름차순 정렬
cars.sort()

# q개의 질의 반복
for _ in range(q):
    # 원하는 연비의 중앙값
    m = int(input())

    # m의 인덱스
    idx = bisect_left(cars, m)

    # m이 자동차 연비 리스트에 없다면 0 출력
    if idx >= n or m != cars[idx]:
        print(0)
        continue

    # 결과: (m의 앞에 있는 자동차의 수) X (m의 뒤에 있는 자동차의 수)
    print(idx * (n - idx - 1))