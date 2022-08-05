import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    num = int(input())
    
    if num != 0:                # arr 원소 추가
        heapq.heappush(arr, (abs(num),num))
                                # num의 절댓값 기준으로 자동 오름차순 정렬
                                # 절댓값이 같으면 num 기준으로 오름차순 정렬     
    else:                       # 절댓값이 가장 작은 수 출력
        if len(arr) == 0:       # 비어있으면 0 출력
            print(0)
        else:
            print(heapq.heappop(arr)[1])
