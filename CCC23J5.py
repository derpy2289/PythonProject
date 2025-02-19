import sys
input = sys.stdin.readline
ans = 0

def dfs(d, x, y, dx, dy, turn):
    if x < 0 or x >= R or y < 0 or y >= C:
        return 0
    if table[x][y] != word[d]:
        return 0
    if d == len(word) - 1:
        return 1
    if not turn and d >= 1:
        return dfs(d + 1, x - dy, y + dx, -dy, dx,True) + dfs(d + 1, x + dy, y - dx, dy, -dx,True) +  dfs(d + 1, x + dx, y + dy, dx, dy, False)
    return dfs(d + 1, x + dx, y + dy, dx, dy, False)




word = input().strip()
R = int(input())
C = int(input())

table = [list(input().strip().split()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        if table[i][j] == word[0]:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (-1,-1), (1,1), (1,-1), (-1,1)]:
                ans += dfs(0, i, j, dx, dy, False)


print(ans)