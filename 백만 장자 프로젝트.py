test_num = int(input())

for i in range(test_num):
    day_num = int(input())
    day_cost = list(map(int, input().split()))

    revenue = 0
    max = day_cost[-1]

    for j in range(day_num-2, -1, -1):
        if(day_cost[j] > max):
            max = day_cost[j]
        revenue += (max - day_cost[j])

    print("#{} {}".format(i+1, revenue))
