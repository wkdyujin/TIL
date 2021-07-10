n, m, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

first = a[n - 1]
second = a[n - 2]

num = m / (k + 1) * k + m % (k + 1)
res = num * first + (m - num) * second

print(res)
