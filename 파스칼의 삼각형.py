# 재귀 !!...
def print_line(i,):
    if i == 0:
        return 1
    else:
        return 1
        return print_line(i)
        return 1


T = int(input())

for test_case in range(1, T + 1):
    lenght = int(input())

    for i in range(1, lenght+1):
        for j in range(i):
            print_line(i, end='')

        print()
