from os import listdir
from time import time
from os import system
from pprint import pprint

inverted_index = {}


def spider(file_paths):
    all_words = []

    with open(file_paths, 'r') as file:
        for line in file.readlines():
            for word in line.strip().split():
                new_word = ''
                for symbol in word.lower():
                    if symbol.isalpha():
                        new_word += symbol
                if new_word:
                    all_words += [new_word]

    return all_words


def indexer(file_path, all_words):
    for word in all_words:
        if word in inverted_index:
            inverted_index[word].add(file_path)
        else:
            inverted_index[word] = {file_path}


def crawler(folder):
    file_paths = set(f'{folder}\\{name}' for name in listdir(folder))
    return file_paths


def search_result(request):
    tmp = set()

    for word in request:
        if word in inverted_index:
            if not tmp:
                tmp = inverted_index[word]
            else:
                tmp = tmp & inverted_index[word]

    return tmp


def main():
    start_time = time()

    folder = 'parts'
    file_paths = crawler(folder)  # создание списка путей к файлам

    for file_path in file_paths:
        all_words = spider(file_path)  # работа паука
        indexer(file_path, all_words)  # работа индексатора

    end_time = time()

    print(f'Время работы поискового робота: {(end_time - start_time):.3f} сек.')

    all_time = 0

    for _ in range(100):  # работа поисковика
        input()
        system('cls')

        request = [word.lower() for word in input('Что ищем: ').split()]

        start_time = time()

        result = search_result(request)

        end_time = time()
        all_time += end_time - start_time

        print(f'Результатов по вашему запросу: {len(result)}')
        print('# Результат поиска #', *result, sep='\n')

    print(f'Время работы поисковика: {all_time:.3f} сек.')


if __name__ == '__main__':
    main()
    # pprint(inverted_index)
