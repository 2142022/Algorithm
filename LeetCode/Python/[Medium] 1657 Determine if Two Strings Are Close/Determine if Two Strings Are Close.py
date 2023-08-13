from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 두 단어의 길이가 같지 않은 경우
        if len(word1) != len(word2):
            return False

        # 두 단어의 구성 알파벳이 다른 경우
        if set(word1) != set(word2):
            return False

        # 단어별로 각 알파벳의 개수 구하기
        c1 = Counter(word1)
        c2 = Counter(word2)

        # 개수들을 list로 바꿨을 때 동일하다면 True, 동일하지 않다면 False 출력
        return sorted(list(c1.values())) == sorted(list(c2.values()))
        