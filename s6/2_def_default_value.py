def save(name, last_name, father_name, age=18, city='rasht'):
    print(name, last_name, father_name, age, city)

for i in range(5):
    a = input("Enter name: ")
    b = input("Enter last name: ")
    c = input("Enter father name: ")
    d = input("Enter age: ")
    e = input("Enter city: (leave blank to set rasht)")
    if e=="" or e=="r" or e=="R":
        save(a, b, c, d)
    else:
        save(a, b, c, d, e)
