"""
:i: количество повторений
функция выполняет вызов самой себя (рекурсию) i раз
"""
def repeat(i):
    tmp=i
    i-=1

    if i<=1:
        print("""2 негритят пошли купаться в море,
        2 негритят резвились на просторе, 
        Один пошел ко дну, второй нашел жену, 
        И вот вам результат... Стало 10 негритят...""")
        return
    
    print("""{} негритят пошли купаться в море,
     {} негритят резвились на просторе,
     Один из них утоп, ему купили гроб
     И вот вам результат - стало {} негритят...""".format(tmp, tmp, i)) #на место {} вставляем параметры tmp, tmp, i
    repeat(i)

repeat(10)

      