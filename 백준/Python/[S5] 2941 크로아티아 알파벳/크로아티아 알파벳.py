import sys
input = sys.stdin.readline

# 단어, 크로아티아 알파벳
word = input().rstrip()
ca = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 각 크로아티아 알파벳을 한 글자로 바꾸기
for i in ca:
    word = word.replace(i,'A')

print(len(word))