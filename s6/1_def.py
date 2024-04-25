import math

def moadele(a, b, c):
    delta = b**2-4*a*c
    if delta<0:
        return "no answer"
    elif delta==0:
        x=-b/(2*a)
        return f"answer is: {x}"
    else:
        x1=(-b-math.sqrt(delta))/(2*a)
        x2=(-b+math.sqrt(delta))/(2*a)
        print('end')
        return f"x1={x1}, x2={x2}"

def alaki():
    for i in range(50):
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        javab=moadele(a, b, c)
        print(javab)

alaki()