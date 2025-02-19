#pa equal first point pb has to be less than half the circlle, pc has to be greater than half the circle  and pa has to be less than half circle from pc

n, c = input().split()
n = int(n)
c = int(c)
point = list(map(int, input().split()))
position = []

for i in range(1, n+1):
    position.append([i, point[i-1]])

for i in range(n):
    a = point[i]
    for j in range(n):
        if point[j] < (c // 2)+a and != a:
            b = point[j]
            for k in range(n):
                if point[k] < (c // 2) + a and != a:
                    
                    c = point[k]
print(position)