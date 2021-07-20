# 패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.
# 스택?

T = int(input())
for i in range(1, T + 1):
    a = input()
    next = a[1:].find(a[0])

    print("#{} {}".format(i, result))
