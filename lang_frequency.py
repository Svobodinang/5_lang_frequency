import sys
import os
import collections


def load_data(filepath):
    try:
        with open(filepath) as text:
            decoded_text = text.read()
            paresed_text = decoded_text.split()
            return paresed_text
    except IOError:
        return None


def get_most_frequent_words(text):
    word_list = []
    for word in text:
        word_list.append(word)

    counter = collections.Counter(word_list)

    return counter.most_common(10)


def input_words(most_frequent_words):
    for number in range(len(most_frequent_words)):
        print("Слово",
              most_frequent_words[number][0],
              "повторяется",
              most_frequent_words[number][1],
              "раз")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit("Вы не ввели путь к файла с данными")
    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        exit("Такого файла не существует")
    if load_data(file_path) is None:
        exit("Проблема с открытием файла")

    text = load_data(file_path)
    most_frequent_words = get_most_frequent_words(text)
    input_words(most_frequent_words)
