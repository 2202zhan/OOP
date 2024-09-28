import math

class Task77e:
    def __init__(self, n):
        # Класс конструкторы, n параметрін инициализациялау
        self.n = n
        
    def calc(self):
        # Нәтижені есептеу әдісі
        res = 1
        s1 = 0
        s2 = 0 
        
        for i in range(1, self.n + 1):  # Класс атрибуты self.n қолданылыпа
            s1 += math.cos(i)  # Косинус мәнін s1-ге қосу
            s2 += math.sin(i)  # Синус мәнін s2-ге қосу
            if s2 != 0:  # Нөлге бөлу қателігін болдырмау үшін тексеру
                res *= s1 / s2
            else:
                res = float('inf')  # Егер s2 нөл болса, res мәнін шексіздікке орнату
                break
        return res

n = int(input("n = "))  # Пайдаланушыдан n мәнін сұрау
t = Task77e(n)  # Task77e классының объектісін жасау
res = t.calc()  # Нәтижені есептеу
print(res)  # Нәтижені шығару
