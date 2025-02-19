word = input()
ans = 0

for i in range(len(word)+1):
    for j in range(len(word)+1):
        palindrome = word[i:j]
        if palindrome == palindrome[::-1]:
            length = len(palindrome)
            if length > ans:
                ans = length

print(ans)