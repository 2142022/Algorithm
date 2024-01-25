# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 전체 문자열, 단축키로 가능한 문자열
    A, B = input().split()

    # A에서 B를 한 글자로 바꾼 후, 길이 세기
    print(f'#{t} {len(A.replace(B, "a"))}')