import sys
import os
import collections


def load_data(filepath):
    try:
        with open(filepath) as text_file:
            readed_text = text_file.read()
            return readed_text
    except IOError:
        return None


def get_most_frequent_words(text):
    word_list = text.split(" ")
    just_word_list = []
    for word in word_list:
        if word.isalpha():
            just_word_list.append(word)
    counter = collections.Counter(just_word_list)
    number_words = 10
    return counter.most_common(number_words)


def output_words(most_frequent_words):
    for word, number in most_frequent_words:
        print("  ",
              word,
              "   - повторяется",
              number,
              "раз(а)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit("Вы не ввели путь к файла с данными")
    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        exit("Такого файла не существует")
    if load_data(file_path) is None:
        exit("Проблема с открытием файла")

    text = load_data(file_path)
    most_frequent_words = get_most_frequent_words(text)
    output_words(most_frequent_words)
