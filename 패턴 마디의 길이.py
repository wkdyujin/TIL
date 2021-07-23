# 패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.
# 1. 스택? xxx
# 2. 앞에서부터 1~10번째 글자까지 잘라서 복사해놓고 비교? 최대 10번 반복함,

T = int(input())
for i in range(1, T + 1):
    s = input()

    for j in range(1, 11):
        split_s = s[:j]
        dup = split_s*2

        print(dup)
        # a ( dup길이까지 index) <--> dup 비교
        if(s[:len(dup)] == dup):
            result = len(dup)//2
            break

    print("#{} {}".format(i, result))
