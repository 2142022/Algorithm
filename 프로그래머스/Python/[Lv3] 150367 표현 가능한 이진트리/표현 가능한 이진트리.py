def solution(numbers):
    # num을 이진트리로 표현 가능한지 구하기
    def isPossible(num):
        # 노드가 1개인 경우 (루트 노드)
        if len(num) == 1:
            # 루트 노드가 0이라면 이진트리로 표현 불가능
            if num[0] == '0':
                return 0
            return 1
        
        # 부모 노드의 존재 여부
        exist = ''

        # 같은 레벨의 노드를 뒤에서부터 2개씩 탐색
        for i in range(len(num) - 1, -1, -4):
            # 자식 노드가 1개 이상 있는데 부모 노드가 없다면 이진트리로 표현 불가
            if (num[i] == '1' or (i - 2 >= 0 and num[i - 2] == '1')) and num[i - 1] == '0':
                return 0
            
            # 부모 노드의 존재 여부 갱신
            exist = num[i - 1] + exist
            if i - 3 >= 0:
                exist = num[i - 3] + exist

        # 부모 노드 레벨 탐색
        return isPossible(exist)

    ###################################################################################################

    # 각 수를 이진수로 변환
    binary = []
    for num in numbers:
        # 이진수로 변환 시 앞의 0b는 삭제
        b = bin(num)[2:]
        
        # 포화이진트리를 만들기 위해 앞에 비어있는 0 채우기
        # 이진수로 변환 했을 때의 길이 = 2^n - 1 이어야 포화이진트리
        # 2^n - 1를 이진수로 나타내면 모두 1로 채워져 있음
        # 이진수로 변환 했을 때의 길이를 이진수로 변환
        bl = bin(len(b))[2:]
        # bl이 모두 1로 채워져 있지 않은 경우 앞에 0 채우기
        if '0' in bl:
            b = '0' * ((1 << len(bl)) - 1 - len(b)) + b
            
        binary.append(b)

    # 각 수의 이진트리로 표현 가능 여부
    result = []
    for num in binary:
        # 재귀를 이용하여 이진트리 표현 가능 여부 구하기
        result.append(isPossible(num))

    return result