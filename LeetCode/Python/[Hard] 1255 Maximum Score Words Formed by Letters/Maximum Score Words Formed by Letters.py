class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # DFS로 최대 점수 합 구하기
        # idx: 현재 탐색할 words의 인덱스
        # score: 현재까지의 점수
        # letters_cnt: 현재 사용할 수 있는 알파벳의 개수
        def dfs(idx, score, letters_cnt):
            # 모든 단어를 다 탐색한 경우 끝내기
            if idx == len(words):
                global max_score
                max_score = max(max_score, score)
                return

            # 현재 단어
            w = words[idx]

            # 현재 사용 가능한 알파벳 복사
            cnt = copy.deepcopy(letters_cnt)

            # 현재 단어를 사용하지 않고 넘어가기
            dfs(idx + 1, score, cnt)

            # 현재 단어를 만들 수 있는지 확인
            possible = True
            w_score = 0
            for i in w:
                if i in cnt:
                    w_score += letters_score[i]
                    cnt[i] -= 1
                    if cnt[i] == 0:
                        cnt.pop(i)
                else:
                    possible = False
                    break
            
            # 현재 단어를 점수에 합하고 다음 단어 탐색
            if possible:
                dfs(idx + 1, score + w_score, cnt)

        ###################################################################

        # letters에 있는 알파벳의 점수
        letters_score = dict()
        
        for alphabet in letters:
            # 이미 딕셔너리에 있다면 패스
            if alphabet in letters_score:
                continue
            
            # 아스키코드를 이용해서 점수 등록
            letters_score[alphabet] = score[ord(alphabet) - ord("a")]

        # 단어 점수 합의 최대값
        global max_score
        max_score = 0

        # DFS로 최대값 구하기
        dfs(0, 0, dict(Counter(letters)))

        return max_score