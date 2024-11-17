# переписала задание module_5_1 - без запроса номера этажа (без go_to)

class House:  # зададим класс House
    # определим метод __init__ с названием и кол-вом этажей
    def __init__(self, name, number_of_floors):
        # присвоим атрибутам названия и кол-ва этажей атрибуты
        self.name = name
        self.number_of_floors = number_of_floors

    # вызвать метод __len__ чтобы определить номер эт.
    def __len__(self):
        return self.number_of_floors
    # вызвать метод __str__ чтобы вывести ин-цию о доме
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


home = House('ЖК Лазурные небеса', 37)

print(home) # вывод ин-ции о доме
print(len(home))  # ранее мы определили что длина = кол-ву эт
