# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії

alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті

for char in alice_in_wonderland:
    if char == "'":
        print(char)

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

black_sea = 436402
azov_sea = 37800
sea_total = black_sea + azov_sea
print(sea_total)


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

storage_1 = 375291 - 222950
storage_3 = 375291 - 250449
storage_total = 375291
storage_2 = storage_total - (storage_1 + storage_3)
print(storage_1)
print(storage_2)
print(storage_3)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

month = 18
monthly_payment = 1179
laptop = monthly_payment * month
print(laptop)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

print(8019 % 8)
print(9907 % 9)
print(2789 % 5)
print(7248 % 6)
print(7128 % 5)
print(19224 % 9)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

pizza_big = 4 * 274
pizza_medium = 2 * 218
juce = 4 * 35
cake = 350
water = 3 * 21
print(pizza_big + pizza_medium + juce + cake + water)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

single_page = 8
photos = 232
print(photos // single_page)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance = 1600
fuel_km = 100
fuel_liter = 9
tank_capacity = 48
total_liters = distance / fuel_km * fuel_liter
total_stops = total_liters // tank_capacity
print("1)",total_liters)
print("2)",total_stops)
