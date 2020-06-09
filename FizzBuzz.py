def FizzBuzz():
    for i in range(0,100):
        if i%3==0 and i%5==0:	#остаток от деления равен 3 или 5?
            print("Fizz")
        elif i%5==0:		#остаток от деления равен 5?
            print("Buzz")
        elif i%3==0:		#остаток от деления равен 3?
            print("FizzBuzz")
        else:
            print(i)
FizzBuzz()
