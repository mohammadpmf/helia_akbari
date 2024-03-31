# dictionaries
numbers = {
    'mohammad': '55555',
    'neda': '22222',
    'helia': '33333',
    'reza': '11111',
    'ali': '44444',
}
# numbers['mohammad']="99999" # برای آپدیت کردن
# name = input("Shoamreye kio mikhay?")
# if name in numbers:
#     print(numbers[name])
# print(numbers.get(name))
for name, number in numbers.items():
    print(f"{name}: {number}")