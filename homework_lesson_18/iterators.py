print("____TASK 1____")
class ReverseIterator:
    """
    reversed list elements
    """
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

my_list = [7, 5, 15, 12, 1]
for item in ReverseIterator(my_list):
    print(item)




print("____TASK 2____")
class EvenIterator:
    """
    returns all even numbers in the range 0 to N
    """
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration

        value = self.current
        self.current += 2
        return value

for num in EvenIterator(15):
    print(num)