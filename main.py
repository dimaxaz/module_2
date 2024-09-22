def find_pairs(n):
    result = []

    for x in range(1, 21):
        for y in range(1, 21):
            if n % (x + y) == 0:
                result.append((x, y))
    return result

# Ввод числа от 3 до 20
n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    pairs = find_pairs(n)
    print("Найденные пары (x, y), для которых n кратно (x + y):")
    for pair in pairs:
        print(pair)
else:
    print("Число должно быть в диапазоне от 3 до 20!")