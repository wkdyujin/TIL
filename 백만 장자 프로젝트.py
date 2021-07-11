test_num = int(input("며칠?:"))

for i in range(test_num):
    day_num = int(input())
    day_cost = list(map(int, input().split()))

    stack = [day_cost[0]]  # 첫날 가격 미리 넣어둠
    revenue = 0

    for j in range(1, day_num):
        if(day_cost[j] >= stack[-1]):  # 오늘이 어제보다 비쌀 경우
            stack.append(day_cost[j])
        else:  # 오늘이 어제보다 쌀 경우 (-->어제 가격으로 다 팔아야 함)
            sell_cost = stack.pop()
            while(len(stack) != 0):  # 스택이 빌 때까지
                revenue += (sell_cost - stack.pop())

    print("#{} {}".format(i+1, revenue))
