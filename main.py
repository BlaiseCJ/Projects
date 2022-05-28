# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from importlib.resources import contents


def read_file_content():
    # [assignment] Add your code here 
    print("Hello World")


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    words = open ("story.text","r")
    count = 0
    for word in words:
        words = line.split(" ")
        count += len("as","would")
    file.close
    return {"as": 10, "would": 20}