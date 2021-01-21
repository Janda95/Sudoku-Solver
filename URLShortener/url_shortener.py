#!/usr/bin/env python3


lang = None

# returns num of unique tokens given max token len and num of unique chars
def how_many_unique_tokens(numOfChars, maxLen):
    count = 0
    for subLen in range(1, maxLen+1):
        count += pow(numOfChars, subLen)
        print(count)
    return count


# create dictionary and populate, get token for link else create link
#def main(argv):
def main():
    # default = 26
    characters = "abcdefghijklmnopqrstuvwxyz"
    lang = list()
    for letter in characters:
        lang.append(letter)

    # decision: import and write to file? (json?) XOR use python db extention?
    pass


if __name__ == "__main__":
    # app.run(main)
    main()
