while True:
    some_string = input()
    if "h" in some_string or "H" in some_string:
        print("'H' present")
        break  # вихід з циклу, якщо літера знайдена
    else:
        print("No 'H'")