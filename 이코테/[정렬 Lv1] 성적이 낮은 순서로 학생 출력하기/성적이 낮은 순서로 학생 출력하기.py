import sys
input = sys.stdin.readline

# 학생 수
N = int(input())

# 학생 이름과 성적 입력받기
student = []
for i in range(N):
    name, score = input().split()
    student.append((score, name))

# 성적 기준으로 오름차순 정렬
student.sort()

# 성적 순으로 이름 출력하기
for i in range(N):
    print(student[i][1], end=' ')
