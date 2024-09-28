import math

class Task77d:
    def __init__(self, n):
        # Конструктор класса для инициализации атрибута n
        self.n = n
    
    def calc(self):
        # Метод для вычисления результата
        res = 0
        for i in range(self.n):  # Используем self.n для доступа к атрибуту класса
            res = math.sqrt(2 + res)  # Вычисляем квадратный корень
        return res

n = int(input("n = "))  # Запрос значения n у пользователя
t = Task77d(n)  # Создание объекта класса Task77d
res = t.calc()  # Вычисление результата
print(res)  # Вывод результата
