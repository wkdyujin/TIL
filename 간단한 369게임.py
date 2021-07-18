T = int(input())
for test_case in range(1, T+1):
    for i in str(test_case):  # 각자릿수 index 접근법
        if(int(i) == 3 or int(i) == 6 or int(i) == 9):
            print("-", end='')
        else:
            print(i, end='')

    if(test_case == T+1):
        continue
    else:
        print(end=' ')  # 줄바꿈x

# 두자리 수 이상일 때 고려
