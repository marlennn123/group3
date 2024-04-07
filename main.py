def count_letter(text):
    letter = "аэеуоиы"
    count = 0

    for char in text.lower():
        if char in letter:
            count += 1
    return count

soz = input("Соз жаз👉: ")
print(count_letter(soz))