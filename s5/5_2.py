while True:
    item = input("Enter item: ")
    if item=='0':
        break
    price= int(input("Enter price: "))
    print(f"Item: {item:20} Price: {price}")
print("Finish")