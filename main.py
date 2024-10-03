example = "Превысокомногорассмотрительствующий"

print("Первый символ: ", example[0])

print("Последний символ: ", example[-1])

half_index = len(example) // 2
second_half = example[half_index:]
print("Вторая половина строки:", second_half)

print("Строка наоборот: ",example [::-1])

print("Каждый второй символ: ", example[1::2])