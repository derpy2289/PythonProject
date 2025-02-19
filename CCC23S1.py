n = int(input())
top = [int(i) for i in input().split()]
bottom = [int(i) for i in input().split()]
tape = 0

for i in range(n):
    if top[i] == 1:
        tape += 3
    if bottom[i] == 1:
        tape += 3

    if i % 2 == 0:
        if top[i] == 1 and bottom[i] == 1:
            tape -= 2

    if i > 0:
        if top[i] and top[i-1]:
            tape -= 1
        if bottom[i] and bottom[i-1]:
            tape -= 1

    if i < n-1:
        if top[i] and top[i+1]:
            tape -= 1
        if bottom[i] and bottom[i+1]:
            tape -= 1

print(tape)



