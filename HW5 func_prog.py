def create_counter(alphabet):
    def count_occurrences(sequence):
        # Генерация словаря для хранения статистики
        # Словарь, в котором ключи - символы из алфавита, а значения - количество вхождений каждого символа в последовательность.
        stats = {char: 0 for char in alphabet}

        # Подсчет встречаемости символов в последовательности
        for char in sequence:
            if char in stats:
                stats[char] += 1

        return stats

    return count_occurrences

# Пример использования функции
alphabet = "abcdefghijklmnopqrstuvwxyz"
count_func = create_counter(alphabet)

sequence = input().lower()
statistics = count_func(sequence)

# Вывод статистики
for char, count in statistics.items():
    print(f"Symbol: {char}, Count: {count}")
