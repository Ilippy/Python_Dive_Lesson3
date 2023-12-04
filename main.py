from collections import Counter
from functools import reduce


# Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.
def get_unique_list(lst: list) -> list:
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


def task1():
    lst = [1, 1, 2, 2, 2, 3, 3, 3, 5, 6, 5, 6, 4, 7, 4]
    print(list(set(lst)))
    print(get_unique_list(lst))


# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях
def is_float(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_one_upper(string: str) -> bool:
    for letter in string:
        if letter.isupper():
            return True
    return False


def task2():
    my_input = input()

    if my_input.isdigit() and (number := int(my_input)) > 0:
        print(f"Целое положительное число {number}")
    elif is_float(my_input) or my_input.isdigit() and int(my_input) < 0:
        print("Вещественное положительное или отрицательное число")
    elif is_one_upper(my_input):
        print("Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква")
    else:
        print("Строку в нижнем регистре в остальных случаях")


# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа
def task3():
    my_tuple = (1, 2, 3.5, 2.6, [12, 5], [35, 2], True, False, {12, 5}, {2, 5})
    my_dict = {}
    for item in my_tuple:
        my_dict.setdefault(type(item), []).append(item)

    print(my_dict)


# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.
def task4():
    lst = [1, 2, 3, 4, 5, 3, 5, 6, 8, 2]
    # 1
    # eddited_lst = [num for num in lst if lst.count(num) != 2]
    # print(f"{eddited_lst = }")
    # 2
    for item in lst[:]:
        if lst.count(item) == 2:
            lst.remove(item)
            lst.remove(item)
    print(f"{lst = }")
    # 3
    # lst = list(filter(lambda x: lst.count(x) != 2, lst))


# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.
def task5():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 5, 3, 1]
    result = [i + 1 for i in range(len(lst)) if lst[i] % 2]
    print(lst, result, sep='\n')


# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.
def task6():
    list_of_strings: list[str] = (input("Введите предложение: ") or "я очень голоден").split()
    max_len = len(max(list_of_strings, key=len))
    for i, word in enumerate(sorted(list_of_strings, key=lambda x: x.encode('utf-8')), start=1):
        print(f"{i} {word:>{max_len}}")


# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.
def task7():
    user_input = input("Введите текст: ") or "abracadabra"
    result = {}
    for letter in user_input:
        result[letter] = result.get(letter, 0) + 1
    print(result)  # Можно использовать Counter в библиотеке collections


# Три друга взяли вещи в поход.
# Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.
def every_one_have(items):
    result = reduce(lambda a, b: set(a) & set(b), items)
    return result


def only_one_have(tour: dict) -> dict:
    result = {}
    for name, items in tour.items():
        temp_set = set(items)
        for key, value in tour.items():
            if key != name:
                temp_set -= set(value)
        if temp_set:
            result[name] = temp_set
    return result


def every_one_have_except_one_v1(tour: dict) -> dict:
    # result = {}
    size = len(tour) - 1
    result = reduce(lambda a, b: Counter(a) + Counter(b), tour.values())
    print(result)
    # for items in set(tour.values()):
    #     for item in items:
    #         result[item] = result.get(item, 0) + 1
    result = dict(filter(lambda pair: pair[1] == size, result.items()))
    for item in result:
        for name, items in tour.items():
            if item not in items:
                result[item] = name
                break
    return result


def every_one_have_except_one_v2(tour: dict) -> dict:
    all_itme = reduce(lambda a, b: set(a) | set(b), tour.values())
    result = {}
    for item in all_itme:
        count, full_name = 0, ''
        for name, items in tour.items():
            if item not in items:
                count += 1
                full_name = name
        if count == 1:
            result[item] = full_name
    return result


def every_one_have_except_one_v3(tour: dict) -> dict:
    result = {}
    for full_name, bag in tour.items():
        temp_set = set()
        for name, items in tour.items():
            if full_name != name:
                temp_set = temp_set & set(items) if temp_set else set(items)
        temp_set -= set(bag)
        for i in temp_set:
            result[i] = full_name
    return result


def task8():
    tour = {"Иван": ("Палатка", "Спальный мешок", "Термос", "Спички", "Еда"),
            "Дмитрий": ("Палатка", "Спальный мешок", "Нож", "Еда"),
            "Василий": ("Спальный мешок", "Еда", "Аптечка", "Посуда")}
    print("У всех есть", ", ".join(every_one_have(tour.values())))
    for name, items in only_one_have(tour).items():
        print(f"Только у {name} есть {', '.join(items)}")
    for item, name in every_one_have_except_one_v3(tour).items():
        print(f"У всех есть {item}, кроме {name}")


def main():
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    # task7()
    task8()


if __name__ == '__main__':
    main()
