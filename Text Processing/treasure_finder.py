key = [int(x) for x in input().split()]

command = input()

while command != "find":
    message = ""
    count = 0

    if command == "find":
        break
    else:
        for char in command:
            char = chr(ord(char) - key[count])
            message += char
            count += 1

            if count == len(key):
                count = 0
    command = input()
    first_type = message.index("&")
    second_type =  message.index("&", first_type + 1)
    element = message[first_type + 1:second_type]
    first_coords = message.index("<")
    second_coords = message.index(">")
    coords = message[first_coords + 1:second_coords]
    count = 0
    print(f"Found {element} at {coords}")
