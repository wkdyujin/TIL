# 1. 단순
n, k = map(int, input().split())
count = 0

while (n != 1):
    if(n % k == 0):
        n /= k
    else:
        n -= 1
    count += 1

print(count)

# 2. 효율 : 배수가 아닐 때 일일히 1씩 빼지x
n, k = map(int, input().split())
result = 0

while (True):
    target = (n // k) * k
    result += (n - target)
    n = target

    if(n < k):
        break

    result += 1
    n //= k

result += (n-1)
print(result)
