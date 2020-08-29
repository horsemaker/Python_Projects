#Interactive English Dictionary
import json
from difflib import get_close_matches

data = json.load(open("data_dictionary.json"))

def meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: #in case user enters like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y/y if YES, or N/n if NO : " % get_close_matches(word, data.keys())[0])
        if yn=="Y" or yn=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word : ")
output = meaning(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)