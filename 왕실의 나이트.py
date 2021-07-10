ans = input()
row, col = ans[0], int(ans[1])

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
n = [1, 2, 3, 4, 5, 6, 7, 8]

row = n[a.index(row)]

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

res = 0

for i in range(len(dx)):
    nx = row + dx[i]
    ny = col + dy[i]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    else:
        res += 1

print(res)
