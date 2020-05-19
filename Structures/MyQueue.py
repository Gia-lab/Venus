class Queue:
        def __init__(self):
                self.items=[]

        def is_empty(self):
                #print("Очередь содержит элементы:")
                return self.items==[]

        def enqueue(self, item):
                
                return self.items.insert(0, item)

        def dequeue(self):
                return self.items.pop()

        def size(self):
                print("Размер очереди ", self.items, " :")
                return len(self.items)
q1=Queue()
print(q1.is_empty())

for i in range (0,7):
        print("В очередь добавлен элемент ", i)
        q1.enqueue(i)
        print(q1.items)

print(q1.size())
