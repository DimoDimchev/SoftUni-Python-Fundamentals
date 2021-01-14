gifts = input()

listGifts = gifts.split(" ")
commandList = []

command = str

while command != "No Money":
    command = input()

    if "OutOfStock" in command:
        commandList = command.split(" ")
        commandList.remove("OutOfStock")
        for i in range(len(listGifts)):
            if commandList[0] in listGifts[i]:
                listGifts[i] = "None"
        commandList = []

    elif "Required" in command:
        commandList = command.split(" ")
        commandList.remove("Required")
        if int(commandList[1]) < len(listGifts) and int(commandList[1]) > 0:
            listGifts[int(commandList[1])] = commandList[0]
        commandList = []

    elif "JustInCase" in command:
        commandList = command.split(" ")
        commandList.remove("JustInCase")
        listGifts[len(listGifts) - 1] = commandList[0]
        commandList = []

for x in range(len(listGifts)):
    if "None" not in listGifts[x]:
        print(listGifts[x], end=" ")
