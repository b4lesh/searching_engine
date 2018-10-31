from os import listdir
from time import time


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


def crawler(folder):
    file_paths = set(f'{folder}\\{name}' for name in listdir(folder))
    return file_paths


def search_result(request, all_words):
    in_text = set()

    for word in all_words:
        if word in request and word not in in_text:
            in_text.add(word)

    if len(in_text) == len(request):
        return True
    return False


def main():
    all_time = 0

    for _ in range(5):
        request = [word.lower() for word in input('Что ищем: ').split()]

        start_time = time()

        result = set()

        folder = 'parts'
        file_paths = crawler(folder)  # работа краулера

        for file_path in file_paths:
            all_words = spider(file_path)  # работа паука
            if search_result(request, all_words):  # работа поисковика
                result.add(file_path)

        end_time = time()
        all_time += end_time - start_time

        print(f'Результатов по вашему запросу: {len(result)}')
        print('# Результат поиска #', *result, sep='\n')

    print(f'Общее время: {all_time:.3f} sec.')


if __name__ == '__main__':
    main()
