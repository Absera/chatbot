import json
import random

with open("data.json") as file:
    data = json.load(file)

def stringify(string):
    # This function removes characters that are inside the 'unwanted_chars' from the 'string' arguement
    word = []
    newString = ""
    unwanted_chars = ["!", "?", ".", ",", "(", ")", "&", ";", '"', "'", "@"]
    stringLength = len(string)

    for char in string:
        word.append(char)
        for unwanted_char in unwanted_chars:
            if unwanted_char in word:
                stringLength -= len(unwanted_char)
                index = word.index(unwanted_char)
                word.pop(index)

    for char in word:
        newString += char
    return newString  # ==> newstring is the string remove all those symbols

running = True
while running:
    userInput = input('> ')
    stringify(userInput)
    print(userInput)
    response = ""
    for dict in data['data']:
        for pattern in dict['input_pattern']:
            if userInput == pattern:
                resp = random.choice(dict['response'])
                print(resp)

    if userInput in data["exit"]["exit_pattern"]:
        running = False
