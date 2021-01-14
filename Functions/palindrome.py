def palindrome(element):
    reversed_element = element[::-1]
    if element == reversed_element:
        return True
    else:
        return False


data = input()
nums_strings = data.split(", ")


for el in nums_strings:
    print(palindrome(el))
