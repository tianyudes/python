# 继承性， 封装性， 多态性
class Human():
    sum = 0
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)

    def do_homework(self):
        print('This is a parent method')


