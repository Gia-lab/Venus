"""
Определение родительского класса Прямоугольник
:параметр a: значение, присваемое переменной width прямоугольника
:параметр b: значение, присваемое переменной height прямоугольника
"""
class Shape():
    def __init__(self, a, b):
        self.width=a
        self.height=b
    def what_i_am(self):
        print("Я - фигура")

"""
Класс Rectangle наследует параметры и методы от класса Shape
"""
class Rectangle(Shape):    
    def calculate_perimeter(self):  #метод вычисления периметра прямоугольника
        print("Периметр прямоугольника со сторонами ", self.width, ",", self.height, "составляет: ", (self.width+self.height)*2) #переменные наследуются из класса Shape
    def what_i_am(self):    #переопределение метода внутри дочернего класса
        print("Я - прямоугольник")
        
"""
Класс Square наследует параметры и методы от класса Shape
"""
class Square(Shape):
    def calculate_perimeter(self):  #метод вычисления периметра квадрата
        print("Периметр квадрата со сторонами ", self.width, "составляет: ", self.width**2) #переменные наследуются из класса Shape
    def change_size(self, a):       #метод изменения размеров сторон квадрата
        self.width+=a
    def what_i_am(self):
        print("Я - квадрат")

"""
Класс Triangle наследует параметры и методы от класса Shape
"""
class Triangle(Shape):
    def calculate_perimeter(self):  #метод вычисления периметра равнобедренного треугольника
        print("Периметр равнобедренного треугольника со сторонами ", self.width, "составляет: ", self.width+self.height*2) #переменные наследуются из класса Shape

r1=Rectangle(10,12)         #создание объекта r1 - прямоугольник со сторонами 10 и 12
r1.calculate_perimeter()
r1.what_i_am()

s1=Square(4,4)              #создание объекта s1 - квадрата со сторонами 4
s1.calculate_perimeter()

s1.change_size(3)           #увеличить сторону квадрата s1 на 3
s1.calculate_perimeter()    #пересчитать периметр квадрата s1
s1.what_i_am()

t1=Triangle(2,4)
t1.calculate_perimeter()
t1.what_i_am()
