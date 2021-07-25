T = int(input())
for i in range(1, T + 1):
    s = input()

    # 마디의 최대 길이가 10이므로 최대 10번 반복
    for j in range(1, 11):
        if(s[:j-1] == s[j:j*2-1]):
            result = j

    print("#{} {}".format(i, result))
