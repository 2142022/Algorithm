def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            return 0
    return 1

T = int(input())
word = []

for i in range(1, T+1):
    word.append(input())

for i in range(1, T+1):
    print('#' + str(i) + ' ' + str(is_palindrome(word[i-1])))
