import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def srch(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter 1 if yes, 2 if no" % get_close_matches(word,data.keys())[0])
        if yn == "1":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "word doesn't exist"
    else:
        return "word doesn't exist"

inp = str.lower(input("enter word to search : "))
outp = srch(inp)

if type(outp) == list:
    for item in outp:
        print(item)
else:
    print(outp)