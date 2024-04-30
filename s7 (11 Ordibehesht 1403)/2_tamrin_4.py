def esm(first, second):
    if first[0]<second[0]:
        first = first[1:]
        if first=="":
            return second    
    elif first[0]>second[0]:
        second = second[1:]
        if second=="":
            return first
    else:
        first = first[1:]
        second = second[1:]
        if first=="" and second=="":
            return "Both strings are empty!"
        elif first=="":
            return second
        elif second=="":
            return first
    first = first[::-1]
    second = second[::-1]
    # print(first)
    # print(second)
    return esm(first, second)

def esm2(first, second):
    while True:
        if first[0]<second[0]:
            first = first[1:]
            if first=="":
                return second    
        elif first[0]>second[0]:
            second = second[1:]
            if second=="":
                return first
        else:
            first = first[1:]
            second = second[1:]
            if first=="" and second=="":
                return "Both strings are empty!"
            elif first=="":
                return second
            elif second=="":
                return first
        first = first[::-1]
        second = second[::-1]

mylist = input("Enter string: ").split()
word = esm(mylist[0], mylist[1])
print(word)
word = esm2(mylist[0], mylist[1])
print(word)