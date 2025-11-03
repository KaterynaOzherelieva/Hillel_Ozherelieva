some_string = input("Please enter a string: ")

some_string_unique = set(some_string)
unique_chars = len(some_string_unique)
if unique_chars > 10:
    print(True)
else:
    print(False)