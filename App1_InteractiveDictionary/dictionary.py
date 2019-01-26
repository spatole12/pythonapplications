import json
import difflib
# from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("data.json"))
# data returns a dictionary
print(type(data))

def meaning(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:              #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]       #in case user enters words like USA or NATO
    elif len(get_close_matches(word,data.keys()))>0:
        #  SequenceMatcher('None',word,data.keys()).ratio()
        # the first word in the reulting list is the one with highest ratio of similarity
        # n is the first n number of closet matches to be displayed
        matched_word = get_close_matches(word,data.keys())[0]
        print(matched_word)
        status = input("Do you mean %s instead..Enter y if yes,n if no" % matched_word)
        if status.lower()=="y":
            return data[matched_word]
        else:
            return "We didnt understand your entry"
    else:
            return "Please enter a valid word!!"
word = input("Enter the word :")
word_meaning = meaning(word)
if(type(word_meaning))== list:
    for meaning in word_meaning:
        print(meaning)
else:
    print(word_meaning)
