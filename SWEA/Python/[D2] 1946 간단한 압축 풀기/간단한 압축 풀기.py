T = int(input())

for i in range(1,T+1):
    print('#' + str(i))

    N = int(input())
    full = ''

    for j in range(N):
        alpha,num = input().split()
        num = int(num)
        full += alpha * num

    for j in range(0, len(full), 10):
        print(full[j:j+10])
