import sys
input = sys.stdin.readline

# N: 도감에 수록되어 있는 포켓몬의 개수, M: 문제의 수
N, M = map(int, input().split())

# 도감
pokemon = []

# N개의 포켓몬 입력받기
for _ in range(N):
    pokemon.append(input().rstrip())

# M개의 문제 맞추기
for _ in range(M):
    # 문제
    find = input().rstrip()

    # 문제의 첫글자가 문자인지 숫자인지 구분
    if ascii('a') <= ascii(find[0]) <= ascii('z') or ascii('A') <= ascii(find[0]) <= ascii('Z'):
        print(pokemon.index(find) + 1)
    else:
        print(pokemon[int(find) - 1])
