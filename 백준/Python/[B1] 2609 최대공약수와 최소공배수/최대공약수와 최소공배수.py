from math import gcd, lcm
import sys
input = sys.stdin.readline

n1, n2 = map(int, input().split())
print(gcd(n1, n2))
print(lcm(n1, n2))