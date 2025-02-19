n = int(input())
tides = list(map(int, input().split()))
ans = []
temp = 0

tides.sort()
if len(tides) % 2 == 1:
    temp = tides[0]
    tides.pop(0)
    n -= 1

mid = n // 2
low = tides[:mid]
low.reverse()
high = tides[mid:]

for i in range(mid):
    ans.append(low[i])
    ans.append(high[i])

if temp != 0:
    print(*ans, temp)
else:
    print(*ans)
