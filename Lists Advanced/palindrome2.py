words = input().split()
searched_word = input()

palindromes = [word for word in words if word == word[::-1]]

# palindromes = []
# for word in words:
#     if word == word[::-1]:
#         palindromes.append(word)

occurances = palindromes.count(searched_word)

print(palindromes)
print(f"Found palindrome {occurances} times")