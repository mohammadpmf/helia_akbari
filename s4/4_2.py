items = {
    'water': 2,
    'coca cola': 4,
    'pizza': 9,
    'pasta': 8,
    'potato': 3,
    'onion': 1
}
for item, price in items.items():
    print(f"{item:<9}: {price}$")
answer = input("what do you need?")
if answer in items:
    amount = int(input(f'how many {answer}?'))
    print(f"Bill: {amount*items[answer]}$")
else:
    print("Sorry. Don't have that item.")
