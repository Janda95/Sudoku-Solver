#!/usr/bin/env python3
# from absl import app
import os
import json

characters = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# returns num of unique tokens given max token len and num of unique chars
def how_many_unique_tokens(numOfChars, maxLen):
    count = 0
    for subLen in range(1, maxLen+1):
        count += pow(numOfChars, subLen)
        print(count)
    return count

# generate token based on count and unique characters
def generate_token(count, lang):
    
    token = "atokenisgenerated"

    return token


# function to add to json
def write_json(data, filename='test.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


# create dictionary and populate, get token for link else create link
# def main(argv):
def main():
    # using file as a dummy db: 1st line how many entries, pairs
    file = None
    if not os.path.exists('test.json'):
        file = open('test.json', 'x')
        file.close()

    file = open('test.json', 'r')
    json_data = json.load(file)
    dataStr = json.dumps(json_data, indent=4)
    print(dataStr)

    lang = list()
    for letter in characters:
        lang.append(letter)

    count = json_data["count"]
    pairs = json_data["urls"]

    urlDict = {}
    for pair in pairs:
        urlDict[pair["website"]] = pair["miniurl"]
    
    myInput = "website.com"
    myUrl = urlDict.get(myInput, None)
    newJsonItem = None

    # create token if dict comes back empty
    if myUrl == None:
        myUrl = generate_token(count, lang)
        urlDict[myInput] = myUrl
        count += 1
        json_data["count"] = count
        newJsonItem = {"website": myInput, "miniurl": myUrl}
        pairs.append(newJsonItem)

    if newJsonItem != None:
        write_json(json_data)

    print(myUrl)


if __name__ == "__main__":
    # app.run(main)
    main()
