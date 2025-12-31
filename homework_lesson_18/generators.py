print("____TASK 1____")
def even_numbers(n):
    """
    Generating even numbers from 0 to N
    """
    for i in range(0, n):
        if i % 2 == 0:
            yield i
for num in even_numbers(30):
    print(num)




print("____TASK 2____")
def fibonacci(n):
    """
    Generating Fibonacci numbers up to N
    """
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

for num in fibonacci(20):
    print(num)