n = int(input())
ans = 0

if n % 4 == 0:
    ans += 1
if n % 5 == 0:
    ans += 1

for i in range(1, n // 4):
    x = i
    if (n - (4*x)) % 5 == 0:
       ans += 1

print(ans)