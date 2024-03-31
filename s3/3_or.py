color = input("Enter your favorite color: ")
# if color=='ghermez' or color == 'red' or color=='Red':
# if color in ['red', 'ghermez', 'Red', 'Ghermez']:
if color.lower() in ['red', 'ghermez']:
    print('red')
else:
    print("Unknown color")
