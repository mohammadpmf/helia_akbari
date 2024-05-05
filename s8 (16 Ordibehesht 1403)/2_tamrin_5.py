# 1- از کاربر ورودی میگیریم. (یک جمله)
# 2- جمله را به کلمات تکی تبدیل میکنیم.
# 3- کلمات را تک تک بررسی می کنیم.
# 4- اگر کلمه بد بود آن را حذف میکنیم.
# 5- اما اگر حرف بدی داشت، کلمه را به خوب تبدیل میکنیم
# 6- کلمات باقی مانده را در خروجی نمایش می دهیم.
import string
def is_good(word):
    good_characters=0
    bad_characters=0
    for character in word:
        if character in string.ascii_letters:
            good_characters += 1
        else:
            bad_characters +=1
    if good_characters<=bad_characters:
        return False
    else:
        return True

def make_good(word):
    good_word = []
    for character in word:
        if character in string.ascii_letters:
            good_word.append(character)
    return ''.join(good_word)

sentence = input("Enter sentence: ")
words = sentence.split()
result = []
for word in words:
    if is_good(word):
        temp = make_good(word.capitalize())
        result.append(temp)
result.sort()
result_dict = {}
for item in result:
    result_dict[item] = result.count(item)
if len(result_dict)==0:
    print('-')
else:
    for k, v in result_dict.items():
        print(k, v)