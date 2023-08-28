from collections import Counter

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # 두 문자열의 각 알파벳 개수가 다른 경우 False
        if Counter(start) != Counter(end):
            return False

        # 두 문자열의 L, R의 순서가 다른 경우 False
        if start.replace('X', '') != end.replace('X', ''):
            return False

        # start에서 L이 있는 인덱스
        startL = []
        # start에서 R이 있는 인덱스
        startR = []
        # end에서 L이 있는 인덱스
        endL = []
        # end에서 R이 있는 인덱스
        endR = []

        # 두 문자열에서 L, R이 있는 인덱스 구하기
        for i in range(len(start)):
            if start[i] == 'L':
                startL.append(i)
            elif start[i] == 'R':
                startR.append(i)
        for i in range(len(end)):
            if end[i] == 'L':
                endL.append(i)
            elif end[i] == 'R':
                endR.append(i)

        # XL -> LX는 되지만, LX -> XL은 안 됨
        # 따라서, start의 L은 end의 L보다 인덱스가 커야 함
        for i, j in zip(startL, endL):
            if i < j:
                return False
        
        # RX -> XR은 되지만, XR -> RX는 안 됨
        # 따라서, start의 R은 end의 R보다 인덱스가 작아야 함
        for i, j in zip(startR, endR):
            if i > j:
                return False

        return True
