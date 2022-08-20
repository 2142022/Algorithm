#문제의 수
N = int(input())

#색 배열로 입력받기
color = list(input())

#색이 바뀌는 인덱스
change = [0]
for i in range(1, N):
    if color[i-1] != color[i]:
        change.append(i)

#양 끝이 같다면 중간을 하나씩 바꾸기
if color[0] == color[N-1] and N > 1:
    cnt = (len(change)-2) // 2 + 2
#양 끝이 다르다면 한 쪽 제외후 하나씩 바꾸기
else:
    cnt = (len(change)-1) // 2 + 2

#기본적으로 한 번은 칠하므로 +1
#len(change)-1 or 2가 홀수이므로 //2를 한 후 +1을 해야함

#len(change)는 처음부터 끝까지 순서대로 색을 바꿨을 경우
print(min(len(change), cnt))
