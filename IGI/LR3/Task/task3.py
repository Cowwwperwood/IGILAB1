from decorators import taskName

@taskName
def task3():
    string = input("please, enter string: ")
    print("number of words starting with a lowercase consonant: ", calculateCountOfSymbols(string))


def calculateCountOfSymbols(string):
    total = 0
    vector_char = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    text = string.split()
    for word in text:
        if (word[0] in vector_char):
            total += 1
    return total