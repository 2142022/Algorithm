from math import isqrt
import sys
input = sys.stdin.readline

# 입력받은 두 정수를 순서대로 정렬
A, B = sorted(map(int, input().split()))

# 두 정수의 행 번호 (0행부터 시작)
rA, rB = isqrt(A - 1), isqrt(B - 1)

# A, B의 열 (1열부터 시작)
cA, cB = A - rA * rA, B - rB * rB

# 두 정수의 행 차이
diff = rB - rA

# A의 열이 홀수인 경우 (바르게 서있는 삼각형인 경우)
if cA % 2:
    # A를 꼭짓점으로 해서 B가 있는 행까지의 정삼각형의 왼쪽 아래 꼭짓점의 열과 오른쪽 아래 꼭짓점의 열
    left, right = cA, cA + 2 * diff

    # B가 정삼각형 안에 있는 경우
    if left <= cB <= right:
        # B가 정삼각형인지, 역삼각형인지에 따라 이동 거리가 달라지므로 cB % 2만큼 더하기
        cnt = 2 * diff - 1 + cB % 2

    # B가 정삼각형의 왼쪽에 있는 경우
    elif cB <= left:
        cnt = 2 * diff + left - cB

    # B가 정삼각형의 오른쪽에 있는 경우
    else:
        cnt = 2 * diff + cB - right

# A의 열이 짝수인 경우 (역삼각형인 경우)
else:
    # A의 왼쪽 삼각형을 꼭짓점으로 해서 B가 있는 행까지의 정삼각형의 왼쪽 아래 꼭짓점의 열과 오른쪽 아래 꼭짓점의 열
    left, right = cA - 1, cA - 1 + 2 * diff

    # B가 정삼각형 안에 있는 경우
    if left <= cB <= right:
        # B가 정삼각형인지, 역삼각형인지에 따라 이동 거리가 달라지므로 cB % 2만큼 더하기
        cnt = 2 * diff + cB % 2

    # B가 정삼각형의 왼쪽에 있는 경우
    elif cB < left:
        cnt = 2 * diff + left - cB + 1

    # B가 정삼각형의 오른쪽에 있는 경우
    else:
        cnt = 2 * diff + cB - right + 1

print(cnt)