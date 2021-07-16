test_num = int(input())

for i in range(test_num):
    day_num = int(input())
    day_cost = list(map(int, input().split()))

    revenue = 0
    max = day_cost[-1]  # 뒤에서부터 풀기! 큰값을 계속 갱신, 작으면 사서 큰값으로 팔음

    for j in range(day_num-1, 0, -1):  # step을 음수로 지정하면 거꾸로 돌아감
        if(day_cost[j] > max):
            max = day_cost[j]
        revenue += (max - day_cost[j])

    print("#{} {}".format(i+1, revenue))
    # ???뭐가 문제지
