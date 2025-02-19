m = int(input())
n = int(input())
table = []

for i in range(m):
    table.append([])
    for j in range(n):
        table[i].append(0)

ans = 0
for i in range(int(input())):
    a, b = input().strip().split()
    b = int(b)-1
    if a == 'R':
        for j in range(n):
            if table[b][j] == 0:
                table[b][j] = 1
                ans += 1
            else:
                table[b][j] = 0
                ans -= 1
    if a == 'C':
        for j in range(m):
            if table[j][b] == 0:
                table[j][b] = 1
                ans += 1
            else:
                table[j][b] = 0
                ans -= 1

print(ans)