x = [input().strip().split() for i in range(int(input()))]
y = [input().strip().split() for i in range(int(input()))]


groups = {}
cnt = 0
for i in range(int(input())):
    a, b, c = input().strip().split()
    groups[a], groups[b], groups[c] = cnt, cnt, cnt
    cnt += 1

ans = 0
for item in x:
    if groups[item[0]] != groups[item[1]]: ans += 1
for item in y:
    if groups[item[0]] == groups[item[1]]: ans += 1

print(ans)