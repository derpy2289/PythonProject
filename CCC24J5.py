import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
pumpkin = {"L": 10, "M":5, "S":1}


def valid(cx, cy):
    return 0 <= cx < row and 0 <= cy < column and table[x][y] != "*" and (x, y) not in visited

def move(x, y, ans=0):
    queue.append((x, y))
    visited.add((x, y))
    while queue:
        px, py = queue.pop(0)

        if table[px][py] != "*":
            ans += pumpkin[table[px][py]]

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = px + dx, py + dy
            if valid(nx, ny):
                queue.append((nx, ny))
                visited.add((nx, ny))
    return ans

table = []
queue = []
visited = set()

row = int(input())
column = int(input())

for i in range(row):
    a = list(input())
    table.append(a)

x = int(input())
y = int(input())

print(move(x, y))

