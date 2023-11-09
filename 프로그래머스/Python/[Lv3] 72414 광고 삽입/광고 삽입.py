def solution(play_time, adv_time, logs):
    # 시, 분, 초를 초로 바꾸기
    def change(h, m, s):
        return h * 3600 + m * 60 + s
    
    ##########################################################################
    
    # 영상 재생 시간 (범위 초과 방지를 위해 + 1)
    h, m, s = map(int, play_time.split(':'))
    playtime = change(h, m, s) + 1
    
    # 영상 재생 시간별 시청자 수
    cnt = [0] * playtime
    for log in logs:
        h1, m1, s1, h2, m2, s2 = map(int, log.replace('-', ':').split(':'))
        # 재생 시작 시간
        start = change(h1, m1, s1)
        # 재생 종료 시간
        end = change(h2, m2, s2)
        cnt[start] += 1
        cnt[end] -= 1
    for i in range(1, playtime):
        cnt[i] += cnt[i - 1]
        
    # 영상 재생 시간별 누적 시청자 수
    for i in range(1, playtime):
        cnt[i] += cnt[i - 1]
        
    # 광고 재생 시간
    h, m, s = map(int, adv_time.split(':'))
    advtime = change(h, m, s)
    
    # 광고가 들어갈 시작 시간
    start = 0
    # 광고 시청자들의 누적 재생시간
    time = cnt[advtime - 1]
    for i in range(1, playtime - advtime):
        t = cnt[i + advtime - 1] - cnt[i - 1]
        if t > time:
            start = i
            time = t

    # 광고 시작 시간을 문자열로 바꾸기
    return '%02d:%02d:%02d'%(start // 3600, start % 3600 // 60, start % 3600 % 60)