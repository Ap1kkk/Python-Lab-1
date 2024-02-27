def find_longest_word(text):
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word

def main():
    print("Выберите способ ввода текста:")
    print("1. Ввести текст через консоль")
    print("2. Считать текст из файла")

    choice = input("Введите номер выбора (1 или 2): ")

    if choice == '1':
        text = input("Введите текст: ")
    elif choice == '2':
        filename = input("Введите имя файла: ")
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read()
        except FileNotFoundError:
            print(f"Файл '{filename}' не найден.")
            return
    else:
        print("Некорректный выбор.")
        return

    longest_word = find_longest_word(text)

    print(f"Самое длинное слово в тексте: '{longest_word}'")

if __name__ == "__main__":
    main()
