import sys
import os

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
        check = False
        for element in word_list:
            if word == element[0]:
                element[1]+=1
                check = True
        if check == False:
            b = [word, 1]
            word_list.append(b)

    number = 1
    while number < len(word_list):
        for index in range(len(word_list) - number):
            if word_list[index][1] < word_list[index + 1][1]:
                word_list[index], word_list[index + 1] = word_list[index + 1], word_list[index]
        number+=1

    if len(word_list) > 10:
        most_frequent_words = []
        for number in range(10):
            most_frequent_words.append(word_list[number])
    else:
        most_frequent_words = [0 * len(word_list)]
        most_frequent_words = word_list

    return most_frequent_words


def input_words(most_frequent_words):
    for number in range(len(most_frequent_words)):
        print("Слово", most_frequent_words[number][0], "повторяется", most_frequent_words[number][1], "раз")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit("Вы не ввели путь к файла с данными")
    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        exit("Такого файла не существует")
    if load_data(file_path) == None:
        exit("Проблема с открытием файла")

    input_words(get_most_frequent_words(load_data(file_path)))
