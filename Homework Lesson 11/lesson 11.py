
def calculate(e):
    try:
        parts = e.split(',')
        numbers = []

        for part in parts:
            clean = part.strip()
            number = int(clean)
            numbers.append(number)

        return sum(numbers)

    except:
        raise ValueError


l = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']

for el in l:
    try:
        result = calculate(el)
        print(result)

    except ValueError:
        print('Не можу це зробити!')