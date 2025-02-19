n = int(input())
height = list(map(int, input().split()))
width = list(map(int, input().split()))
area = 0

for i in range(n):
    area += width[i] * (height[i]+height[i+1]) / 2.0

print(area)