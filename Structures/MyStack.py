class Stack:
    def __init__(self):
        self.items=[]           #стек

    def is_empty(self):
        print("Стек пустой: ")
        return self.items==[] #если стек пустой, то метод возвращает True, иначе - False

    def push(self, item):
        print("В стек добавлен элемент:", item)
        self.items.append(item) #добавить в конец стека элемент item
        print("Содержимое стека: ", self.items)
        print("\n")

    def pop(self):
        a=self.items.pop()
        print("Удален последний элемент стека", a)
        return a #удалить последний элемент из стека

    def peek(self):
        last=len(self.items)-1  #индекс последнего элемента, помещенного в стек
        print("Последний элемент в стеке:")
        return self.items[last] #значение последнего элемента в стеке

    def size(self):
        print("Размер стека: ")
        return len(self.items)  #размер стека
          
def rev(d):
    print("=============================================================")
    s=Stack()
    for i in d:
        s.push(i)
    print("Пошаговое выполнение реверса стека: ", s.items)    
    x=""
    
    for i in range(len(s.items)):
        x+=s.pop()
    print("Стек наоборот: ", x)
    
st1=Stack()
print (st1.is_empty())
st1.push("start")
st1.push("a2")
print (st1.is_empty())
print (st1.pop())
print (st1.is_empty())
for i in range (2, 9):
    st1.push(i)

print(st1.size())
print(st1.peek())

rev("Привет")
rev("Здорово")
rev("12345")
