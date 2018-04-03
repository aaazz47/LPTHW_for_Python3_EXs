def break_words(stuff):
    """
    This function will break up words for us.
    这个函数会为我们拆分出单词。
    """
    words = stuff.split(' ')
    return words

def sort_words(words):
    """
    Sorts the words.
    对单词进行排序
    """
    return sorted(words)

def print_first_word(words):
    """
    Prints the first word after popping it off.
    抛出第一个单词并打印
    """
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """
    Print the last word after popping it off.
    抛出最后一个单词并打印
    """
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """
    Takes in a full sentence and returns the sorted words.
    输入完整的句子，并返回排序后的单词。
    """
    words = break_words(sentence)
    return sort_words(words)

def print_first_adn_last(sentence):
    """
    Prints the fist and last words of the sentence.
    打印句子的第一个和最后一个单词。
    """
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_list_sorted(sentence):
    """
    Sorts the words then prints the first and last one.
    句子排序后打印第一个和最后一个单词
    """
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
