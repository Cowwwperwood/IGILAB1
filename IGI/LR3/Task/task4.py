from inputfunctions import inputCheck, TYPES
from decorators import taskName

sentense = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and "\
         "stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking "\
         "the daisies, when suddenly a White Rabbit with pink eyes ran close by her."


def calculateWordsWithMinimumLength(sentense):
    sentense = sentense.split()
    min_len = 100
    total_minlen = 0
    for word in sentense:
        if (len(word) < min_len):
            min_len = len(word)
    for word in sentense:
        if (len(word) == min_len):
            total_minlen += 1
    return total_minlen


def wordsWithDot(sentense):
    sentense = sentense.split()
    word_dot = []
    for word in sentense:
        if (word[-1] == '.'):
            word_dot.append(word)
    return word_dot


def longestWordWithR(sentense):
    sentense = sentense.split()
    maxlen_word_r = ''
    for word in sentense:
        if (word[-1] == 'r' and len(word) > len(maxlen_word_r)):
            maxlen_word_r = word
    return maxlen_word_r


@taskName
def task4():
    while True:
        choice = inputCheck("please, enter option from 1 to 3 or '0' to exit: ", TYPES.INT)
        match choice:
            case 1:
                print("Number of words with minimum length:", calculateWordsWithMinimumLength(sentense))
            case 2:
                print("Number of words with dot:", wordsWithDot(sentense))
            case 3:
                print("Longest word with r: ", longestWordWithR(sentense))
            case 0:
                return
            case _:
                print("incorrect input.")
                continue
