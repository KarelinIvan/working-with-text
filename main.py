import re

list_words = []
print(type(list_words))

# Читаем файл, убираем знаки преписания и записываем слова в
with open("pg79633.txt", "r", encoding="utf-8") as file:
    line = file.read()
    patterns = r"[!,.?;:#$%^&*(),]"
    clear_line = re.sub(patterns, "", line).lower()

    list_words = clear_line.split()

col_words = len(list_words)
print(f"Количество слов в книге:{col_words}")

unique_words = set()

for i in list_words:
    unique_words.add(i)

col_uni_words = len(unique_words)
print(f"Количество уникальных слов в книге:{col_uni_words}")


# print(list_words)
