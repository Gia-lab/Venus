"""
Определение класса Прямоугольник
:параметр a: значение, присваемое переменной width прямоугольника
:параметр b: значение, присваемое переменной height прямоугольника
"""
class Rectangle():
    def __init__(self, a, b):    #self - объект, a, b - значения переменных width, height объекта self 
        self.width=a
        self.height=b
        
    def calculate_perimeter(self):  #метод вычисления периметра прямоугольника
        print("Периметр прямоугольника со сторонами ", self.width, ",", self.height, "составляет: ", (self.width+self.height)*2)

"""
Определение класса Квадрат
:параметр a: сторона квадрата
"""
class Square():
#        square_list=[]
    
    def __init__(self, a):
        self.width=a
#        self.square_list.append(self.width)

    def calculate_perimeter(self):  #метод вычисления периметра квадрата
        print("Периметр квадрата со сторонами ", self.width, "составляет: ", self.width**2)

    def change_size(self, a):       #метод изменения размеров сторон квадрата
         self.width+=a
#    def __repr__(self):
#        return print("Квадрат ", self.width, " на ", self.width)

r1=Rectangle(10,12)         #создание объекта r1 - прямоугольник со сторонами 10 и 12
r1.calculate_perimeter()

s1=Square(4)                #создание объекта s1 - квадрата со сторонами 4
s1.calculate_perimeter()
#print(s1)

s1.change_size(3)           #увеличить сторону квадрата s1 на 3
s1.calculate_perimeter()    #пересчитать периметр квадрата s1

"""
функция сравнения двух объектов
:параметр a: объект1
;параметр b: объект2
:return: результат сравнения объектов
"""
def compare(a, b):
    return print("Объекты \"", a, "\" и \"", b, "\" идентичны: ", (a is b))

compare(s1, s1)
compare("Солнце", "солнце")
