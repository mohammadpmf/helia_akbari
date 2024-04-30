# 1- voroodi ra ke adade 2 raghami hast migirim.
# 2- do ragham ra az ham joda mikonim.
# 3- do adad ra az ham kam mikonim.
# 4- ghadre motlagh ra migirim
# 5- javab ra print kon.
def two_digits(number):
    if number>99 or number<10:
        return f"{number} is not a 2 digit number!"
    a = number//10
    b = number%10
    answer = a-b
    javab = abs(answer)
    return javab

number = input("Enter a 2 digit number: ")
if number.isdigit():
    number=int(number)
    print(two_digits(number))
else:
    print(f"{number} is not really a number!")


