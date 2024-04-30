print('ok')
try:
    a = int(input("Enter number a:"))
    b = int(input("Enter number b:"))
    print(f"{a}/{b}={a/b}")
except ZeroDivisionError:
    print("can not divde by zero")
except ValueError:
    print("you did not enter a real number")

print("Other parts of program")
