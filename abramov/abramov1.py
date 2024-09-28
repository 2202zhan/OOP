import math

#abramov 77
class Taskffg:
    def __init__(self, n): 
        self.n = n

    def calc(self):
        res = 0
        sum_val = 0  
        for i in range(1, self.n + 1):  
            sum_val = sum_val + math.sin(i)  
            res = res + 1 / sum_val  
        return res

n = int(input("Введите n: "))  
taskffg = Taskffg(n)
res = taskffg.calc()
print(res)
