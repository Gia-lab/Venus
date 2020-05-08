#импорт готовых модулей Python
import math #импорт модуля математичеких функций
import random #импорт модуля рандомного поиска
import statistics #импорт модуля статистических расчётов
import keyword #импорт модуля ключевых слов

"""
Функция возводит a в степень b
:параметр a: число
:параметр b: степень
"""
def pow_a_b(a,b):
    print(a, " в степени ", b, "=", pow(3,4))

"""
Функция выбирает рандомное число из диапазона от a до b
:параметр a: начало интервала
:параметр b: конец интервала
"""
def randomize(a,b):
    print("Рандомное число из диапазона ", a, "-", b, ":", random.randint(a,b))
    
list1=[6, 8, 12, 90, 7, 34] #выборка чисел

def statdata(s):
    x1=statistics.mean(s)   #среднее из выборки чисел
    x2=statistics.median(s) #медиана из выборки чисел
    x3=statistics.mode(s)   #мода из выборки чисел
    print("Среднее из диапазона чисел", x1)
    print("Медиана из диапазона чисел", x2)
    print("Мода из диапазона чисел", x3)

def defkey(w):
    print("Введено слово", w, ", оно ключевое в языке Python: ", keyword.iskeyword(w))

pow_a_b(3,4)
randomize(20, 30)
statdata(list1)
defkey("print")
defkey("def")
