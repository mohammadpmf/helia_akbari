# 1-character avval ra barresi kon
# agar U bood. 1 vahed ezafe kon
# agar D bood. 1 vahed kam kon.
# agar N bood. kari nakon.
# 0
# "UDNUUD"

def find_tabaghe():
    string = input("Enter string: ")
    tabaghe=0
    for i in range(6):
        character = string[i]
        if "U"==character:
            tabaghe = tabaghe+1
        elif character=="D":
            tabaghe = tabaghe-1
    return tabaghe

def find_tabaghe_2():
    string = input("Enter string: ")
    tabaghe=0
    for i in string:
        if "U"==i:
            tabaghe = tabaghe+1
        elif i=="D":
            tabaghe = tabaghe-1
    return tabaghe

print(find_tabaghe_2())