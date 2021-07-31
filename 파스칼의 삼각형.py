# 어케해야하지

T = int(input())

for test_case in range(1, T + 1):
    lenght = int(input())
    top = 1

    for i in range(1, lenght+1):
        for j in range(i):
            print(top, end='')
        print()
