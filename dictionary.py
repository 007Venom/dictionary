import json
from difflib import get_close_matches
data = json.load(open("original.json"))


def translate(w):
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(" Did you mean this word %s ? 'Y' if yes or 'N' for no." %
                   get_close_matches(w, data.keys())[0])
        if yn == 'Y' or yn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'N' or yn == 'n':
            return "No such word could be found.Please check the word again"
        else:
            return "You entered someone other word which could not be understood."

    else:
        return "Wrong word.Please double check it."


word = input("Enter a word:   ").lower()
output = translate(word)
if type(output) == list:
    for letter in output:
        print(letter)
else:
    print(output)
