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


# create dictionary and populate, get token for link else create link
# def main(argv):
def main():
    # using file as a dummy db: 1st line how many entries, pairs
    file = None
    if not os.path.exists('test.json'):
        file = os.open('test.json', 'rwx')

    lang = list()
    for letter in characters:
        lang.append(letter)

    #json_data = json.load(file)
    # dataStr = json.dumps(json_data)
    
    data = {'people': [{'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}]}
    dataStr = json.dumps(data)
    print(dataStr)
    # for item in json_data:
    #     print("")

    # decision: import and write to file? (json?) XOR use python db extention?
    pass


if __name__ == "__main__":
    # app.run(main)
    main()
