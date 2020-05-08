import math

"""
Определение класса Apple()
"""
class Apple():
    def __init__(self, a, b, c, d): #инициализация переменных a, b, c, d экземпляра, заданного переменной self 
        self.variety=a  #переменная variety - сорт
        self.taste=b    #переменная taste - вкус
        self.color=c    #переменная color - цвет
        self.size=d     #переменная size - размер
        print("Яблоко сорта ", a, "имеет ", b, " вкус,", c, " цвет и ", d, "размер") 

a1=Apple("Голден", "кислый", "зелёный", "средний")  #a1 - экземпляр класса Apple()
a1.color="жёлтый"
print(a1.color)

"""
Определение класса Circle()
"""
class Circle():
    def __init__(self, r):  #при содании экземпляра класса (объекта) небходимо указать радиус
        self.radius=r       #переменной radius объекта присвоить значение r
        
    def area(self): #метод выводит площадь круга
        print("Площадь круга с радиусом ", self.radius, " составляет ", math.pi*self.radius**2)

c1=Circle(5)    #создание объекта c1 с параметром (радиус=5) класса Circle
c1.area()

"""
Определение класса Triangle()
"""
class Triangle():
    def __init__(self, a, b):
        self.width=a    #основание треугольника width принимает значение параметра a
        self.height=b   #высота треугольника height принимает значение параметра b

    def area(self):     #метод выводит площадь треугольника
        print("Площадь треугольника с шириной ", self.width, " и высотой ", self.height, "составляет ", self.width*self.height/2)

t1=Triangle(3,5)
t1.area()

"""
Определение класса Hexagon()00..
"""
class Hexagon():
    def __init__(self, a, b, c, d, e, f):
        self.a1=a   #сторона a1
        self.a2=b   #сторона a2
        self.a3=c   #сторона a3
        self.a4=d   #сторона a4
        self.a5=e   #сторона a5
        self.a6=f   #сторона a6
        
    def calculate_perimeter(self):  #вывести на экран периметр шестиугольника
        print("Периметр шестиугольника со сторонами ", self.a1, self.a2, self.a3, self.a4, self.a5, self.a6, " составляет: ", self.a1+self.a2+self.a3+self.a4+self.a5+self.a6)

h1=Hexagon(4,2,5,6,1,4)
h1.calculate_perimeter()


