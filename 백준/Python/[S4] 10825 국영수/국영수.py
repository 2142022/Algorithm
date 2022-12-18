import sys
input = sys.stdin.readline

# 학생 수
N = int(input())

# N명의 학생의 이름, 국어, 영어, 수학 점수 입력받기
student = []
for _ in range(N):
    name, korean, english, math = input().split()

    # 국어, 영어, 수학 점수는 int형으로 바꾸기
    korean = int(korean)
    english = int(english)
    math = int(math)

    student.append((name, korean, english, math))

# 조건에 맞게 정렬하기
student.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

# 정렬된 순서로 학생 이름 출력하기
for i in student:
    print(i[0])