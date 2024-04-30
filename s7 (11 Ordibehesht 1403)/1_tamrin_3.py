# به عنوان ورودی یک لیست از اعداد میگیریم.
# اعداد زوج را جدا میکنیم و در یک لیست میگذاریم.
# اعداد فرد را جدا میکنیم و در لیست دوم میگذاریم.
# هر دو لیست را پرینت میکنیم.
a = input("Enter string: ").split()
ali = []
reza = []
for i in a:
    if int(i)%2==0:
        ali.append(i)
    else:
        reza.append(i)
if len(ali)!=0:
    print(' '.join(ali))
else:
    print(ali)
if len(reza)!=0:
    print(' '.join(reza))
else:
    print(reza)