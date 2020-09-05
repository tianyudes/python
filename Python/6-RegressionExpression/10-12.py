import re
s = 'A67b6t6sa44h57ja23sh8jh45hh45js8h'


def convert(value):
    a = value.group()
    if int(a) > 20:
        return '99'
    else:
        return '0'


r = re.sub('\d{1,2}', convert, s)
print(r)