"""
Определение класса Horse
:параметр hname: имя лошади
:параметр rname: имя владельца
"""
class Horse():
    def __init__(self, hname, rname="Имя"):
        self.hn=hname
        self.rn=rname
        print("Лошадь ", self.hn, " принадлежит ", self.rn)

"""
Определение класса Rider
:параметр name: имя наездника
"""
class Rider():
    def __init__(self, name):
        self.rnew=name
    def __repr__(self):     #переопределение магического метода __repr__, который наследуется от родительского класса Object 
        return self.rnew

r1=Rider("Leo")
o1=Horse("Belle", r1)   

print(o1.rn.rnew)   #считывание значения rnew класса Horse через присвоение её переменной rn класса Horse
