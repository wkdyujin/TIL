n, m = map(int, input().split())
res = 0

for i in range(n):
    a = list(map(int, input().split()))
    if(min(a) > res):
        res = min(a)

print(res)
