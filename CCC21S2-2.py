m = int(input())
n = int(input())
row = [0] * m
column = [0] * n

for i in range(int(input())):
    a, b = input().strip().split()
    b = int(b)-1
    if a == 'R':
        row[b] += 1
    if a == 'C':
        column[b] += 1

true_row = sum([0 if x % 2 != 1 else 1 for x in row])
true_column = sum([0 if x % 2 != 1 else 1 for x in column])


print(true_row * n + true_column * m - 2 * true_row * true_column)