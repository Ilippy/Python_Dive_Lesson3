items = {
    "лодка": 3.0,
    "велосипед": 4.0,
    "мангал": 2.0
}
max_weight = 2.0

import warnings

warnings.filterwarnings('ignore')

# При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0

# Введите ваше решение ниже
backpack = {}
for key, value in items.items():
    if max_weight - value >= 0:
        backpack[key] = value
        max_weight -= value

# print(backpack)


max_weight = 2.0
backpacks_test = []
sorted_result = []
for i in range(2 ** len(items)):
    backpack_test = {}
    weight = 0
    for j, item in enumerate(items):
        if i & (1 << j):
            if weight + items[item] <= max_weight:
                backpack_test[item] = items[item]
                weight += items[item]
            else:
                break
    backpacks_test.append(backpack_test)

full_result = [backpack_test for backpack_test in backpacks_test if backpack_test]
result = []
for item in full_result:
    if item not in result:
        result.append(item)

x = 0
for i in result:
    print(dict(sorted(i.items(), key=lambda item: item[1], reverse=True)))
    print(dict(sorted(backpack.items(), key=lambda item: item[1], reverse=True)))
    if dict(sorted(i.items(), key=lambda item: item[1], reverse=True)) == dict(
            sorted(backpack.items(), key=lambda item: item[1], reverse=True)):
        x += 1
if x > 0:
    print(True)
else:
    print(False)