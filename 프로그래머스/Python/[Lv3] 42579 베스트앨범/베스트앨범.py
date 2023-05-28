import heapq

def solution(genres, plays):
    # 노래 개수
    S = len(genres)
    # 장르 개수
    G = 0

    # 장르별 재생 횟수
    cnt = {}
    # 장르별 노래와 재생 횟수
    song = {}

    # 한 곡씩 확인하기
    for i in range(S):
        # 새로운 장르인 경우
        if genres[i] not in cnt:
            # 현재 곡의 재생 횟수로 등록
            cnt[genres[i]] = plays[i]
            # 현재 곡의 재생 횟수와 번호 등록
            song[genres[i]] = [(-plays[i], i)]
            # 장르 개수 추가
            G += 1

        # 기존에 있던 장르인 경우
        else:
            # 현재 곡의 재생 횟수만큼 추가
            cnt[genres[i]] += plays[i]
            # 현재 곡의 재생 횟수와 번호 추가
            heapq.heappush(song[genres[i]], (-plays[i], i))

    # 재생횟수 기준으로 정렬한 장르
    order = sorted(cnt.items(), key=lambda x: x[1], reverse=True)

    # 베스트 앨범
    result = []

    # 장르별로 두 곡씩 추가하기
    for i in range(G):
        # 현재 장르
        g = order[i][0]

        # 현재 장르에서 상위 2개 넣기
        for j in range(2):
            result.append(heapq.heappop(song[g])[1])

            # 노래가 한 곡이라면 끝내기
            if not song[g]:
                break

    return result