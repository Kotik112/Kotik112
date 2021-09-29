try:
    n = int(input("Enter the number: "))
    i = 1
    for i in range(n+1):
        if  ((i % 3) == 0) and ((i % 5) == 0):
            print("FizzBuzz")
            continue
        elif (i % 5) == 0:
            print("Buzz")
            continue
        elif (i % 3) == 0:
            print("Fizz")
            continue

except ValueError as e:
    print("The program strictly accepts integer inputs.")
    print(e)
except ZeroDivisionError as e:
    print("Division by Zero")
    print(e)
    
