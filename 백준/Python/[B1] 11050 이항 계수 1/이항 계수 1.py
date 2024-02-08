from itertools import combinations
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
print(len(list((combinations(range(N), K)))))