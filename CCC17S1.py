n = int(input())

row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))

ans = 0
score1 = 0
score2 = 0

for i in range(n):
    score1 += row1[i]
    score2 += row2[i]
    if score1 == score2:
        ans = i+1

print(ans)