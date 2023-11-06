test_string = "pereiro_loves_python"

def ignore_space(string):

    cleaned_string = string.replace("_", "").replace(" ", "")

    num_letters = len(cleaned_string)

    return num_letters

num_letters = ignore_space(test_string)

print("Значение переменной test_string:", test_string)
print("Количество букв в строке (игнорируя _ и пробелы):", num_letters)

