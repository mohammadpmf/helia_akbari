# 1- voroodi ra ke adade 2 raghami hast migirim.
# 2- do ragham ra az ham joda mikonim.
# 3- do ragham ra moghayese mikonim.
# 4- adade bozorgtar ra entekhab mikonim
# 5- adade koochaktar ra az an kam mikonim.
# 6- javab ra print kon.
def two_digits(number):
    if number>99 or number<10:
        return f"{number} is not a 2 digit number!"
    a = number//10
    b = number%10
    bozorgtar = b
    if a>b:
        bozorgtar=a
    koochektar=a
    if b<a:
        koochektar=b
    javab = bozorgtar-koochektar
    return f"{bozorgtar}-{koochektar}={javab}"

number = input("Enter a 2 digit number: ")
if number.isdigit():
    number=int(number)
    print(two_digits(number))
else:
    print(f"{number} is not really a number!")

