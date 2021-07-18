N = int(input())

for i in range(1, N+1):
    clap = 0
    for j in str(i):  # 각자릿수 순회
        if(j == '3' or j == '6' or j == '9'):
            clap += 1

    if (clap > 0):
        i = '-' * clap
    print(i, end=' ')  # 줄바꿈x
