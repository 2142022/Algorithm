N = int(input())
stack = []

for i in range(N):
    option = input()

    #숫자 넣기
    if "push" in option:
        order, num = map(str, option.split())
        stack.append(int(num))

    #마지막 원소 뽑기(원소가 없으면 -1 출력)
    elif option == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    #리스트 길이 출력
    elif option == "size":
        print(len(stack))

    #원소가 없으면 1, 있으면 0출력
    elif option == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    #마지막 원소 출     
    elif option == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
