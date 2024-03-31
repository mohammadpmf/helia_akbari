foods = ['Chicken', 'pizza', 'hamburger', 'frenchfries', 'pizza', 'cheicken', 'kebab',
         'pizza', 'hamburger', 'sausege', 'french fries', 'pasta', 'pizza', 'pizza',
         'hamburger', 'pasta', 'lasania', 'pizza']

foods2 = ['Chicken', 'pizza', 'hamburger', 'frenchfries', 'pizza', 'kebab', 'kebab',
         'kebab', 'kebab', 'sausege', 'kebab', 'pasta', 'pizza', 'kebab',
         'hamburger', 'pasta', 'kebab', 'pizza']

def my_index(my_list, my_item):
    x = my_list.count(my_item)
    print(x)
    temp = []
    i=-1
    for k in range(x):
        i=my_list.index(my_item, i+1)
        temp.append(i)
    print(temp)
# اول ۲ تا لیست رو با همدیگه ادغام کنید (منظور extend است.)
# در مرحله بعد ۳ غذا را بپرسید و از داخل لیست حذف کنید ( با استفاده از remove)
# نام غذایی پرسیده شود و تعداد باقیمانده از آن غذا چاپ شود.
# شماره خانه جایی که غذا پیدا شده هم پرینت شود.

foods.extend(foods2)
food = 'pizza' #input("Which one?")
my_index(foods, 'pasta')
my_index(foods, 'pizza')
my_index(foods, 'Chicken')
# x = foods.count(food)
# print(x)
# i=-1
# for k in range(x):
#     i=foods.index(food, i+1)
#     print(i)

# print(foods)
