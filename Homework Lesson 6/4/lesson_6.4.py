some_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
even_numbers = []
for number in some_numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(sum(even_numbers))