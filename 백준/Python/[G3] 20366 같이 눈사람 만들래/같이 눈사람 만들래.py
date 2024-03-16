import sys

input = sys.stdin.readline


# 최소 키 차이 구하기
def get_diff():
    # 최소 키 차이
    diff = 4 * H[-1]

    # 엘자 눈 2개
    for i in range(N - 3):
        e1 = H[i]
        for j in range(i + 3, N):
            e = e1 + H[j]

            # 안나 눈 2개
            left, right = i + 1, j - 1
            while left < right:
                a = H[left] + H[right]

                # 둘의 키가 같은 경우
                if a == e:
                    return 0

                # 키 차이 비교
                diff = min(diff, abs(a - e))

                # 엘자 눈사람 키가 더 큰 경우
                if a < e:
                    left += 1
                # 안나 눈사람 키가 더 큰 경우
                else:
                    right -= 1

    return diff


####################################################

# 눈 개수
N = int(input())

# 눈 지름 크기 (오름차순 정렬)
H = sorted(list(map(int, input().split())))

print(get_diff())