def anagram(a,b):
    a1=a.lower()    #перевод в нижний регистр
    b1=b.lower()
    if (a1==b1):
        print("Введено одно и то же слово: ", a)
    elif (sorted(a1)==sorted(b1)):  #сортировка букв в слове по алфавиту
        print ("\"", a1, "\" и ", "\"", b1, " \" являются анаграммами")

anagram("кот", "ток")
anagram("ток", "ток")
