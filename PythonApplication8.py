def split_digits_and_letters():
    raw_input = input("Введіть елементи списку через пробіл (наприклад: a 1 b 23 c 4 d): ")
    original_list = raw_input.split()

    digits_list = []
    letters_list = []

    for item in original_list:
        if item.isdigit():
            digits_list.append(int(item))
        elif item.isalpha():
            letters_list.append(item)
        else:
            # Якщо елемент змішаний (наприклад, "a1"), розбираємо його посимвольно
            for char in item:
                if char.isdigit():
                    digits_list.append(int(char))
                elif char.isalpha():
                    letters_list.append(char)

    print("\n--- Результати роботи зі списками ---")
    print(f"Початковий список: {original_list}")
    print(f"Список цифр/чисел: {digits_list}")
    print(f"Список літер:      {letters_list}")

if __name__ == "__main__":
    split_digits_and_letters()
