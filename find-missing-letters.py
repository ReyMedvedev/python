def find_missing_ukrainian_letters(text):
    text = text.lower()
    ukrainian_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    alphabet = set(ukrainian_alphabet)
    text_letters = set(text)
    missing_letters = alphabet - text_letters
    missing_letters = sorted(list(missing_letters))
    return missing_letters

text = "Привіт, світ!"
missing_letters = find_missing_ukrainian_letters(text)

if missing_letters:
    print("The following Ukrainian letters are missing:", ", ".join(missing_letters))
else:
    print("The text contains all Ukrainian letters of the alphabet.")
