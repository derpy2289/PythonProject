import sys

read_input = sys.stdin.readline  # Renamed for clarity
ans = 0

# Define all possible directions for movement
DIRECTIONS = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]


def dfs(depth, x, y, dx, dy):
    # Base cases:
    if x < 0 or x >= R or y < 0 or y >= C:  # Out of bounds
        return 0
    if table[x][y] != word[depth]:  # Character mismatch
        return 0
    if depth == len(word) - 1:  # Successfully matched the entire word
        return 1

    # Recursive case: keep searching in the same direction
    return dfs(depth + 1, x + dx, y + dy, dx, dy)


def call_dfs_in_all_directions(start_x, start_y):
    total = 0
    for dx, dy in DIRECTIONS:  # Iterate through all directions
        total += dfs(0, start_x, start_y, dx, dy)
    return total


# Input processing
word = read_input().strip()
R = int(read_input())
C = int(read_input())

table = [list(read_input().strip().split()) for _ in range(R)]

# Main loop to search for the word
for i in range(R):
    for j in range(C):
        if table[i][j] == word[0]:  # Match first character of the word
            ans += call_dfs_in_all_directions(i, j)

print(ans)
