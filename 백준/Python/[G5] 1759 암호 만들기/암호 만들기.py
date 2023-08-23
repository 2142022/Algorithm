from itertools import combinations
import sys
input = sys.stdin.readline

# L: 암호의 길이, C: 사용 가능한 알파벳 개수
L, C = map(int, input().split())

# 사용 가능한 알파벳
alphabet = list(input().split())
# 오름차순 정렬
alphabet.sort()

# 모음
vowel = ('a', 'e', 'i', 'o', 'u')

# 알파벳 L개씩 뽑기
for alpha in combinations(alphabet, L):
    # 모음 개수
    vc = 0
    # 자음 개수
    cc = 0

    # 모음 개수, 자음 개수 세기
    for i in alpha:
        if i in vowel:
            vc += 1
        else:
            cc += 1

    # 모음이 1개 이상, 자음이 2개 이상인 경우에만 암호 가능
    if vc >= 1 and cc >= 2:
        print(''.join(alpha))
