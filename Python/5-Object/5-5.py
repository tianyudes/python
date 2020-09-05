# 现在Student类想要继承People这个类
from c4 import Human


class Student(Human):
    school = ''
    class_number = ''
    grade = ''

    def __init__(self, school,grade, class_number, name, age):
        self.school = school
        self.grade = grade
        self.class_number = class_number
        # Human.__init__(self, name, age) # 在子类里面调用父类的构造方法，这个相当于自己调用，所以要把所有的变量都放上去，要让系统知道传进去的是谁，后面有一个例子。但是这个很麻烦
        # 尤其在更改父类名称的时候，就要修改的地方有点多。所以推荐以下的方法：
        super(Student,self).__init__(name,age)

    def do_homework(self):
        super(Student,self).do_homework()
        print(str(self.name) + ' is doing homework')


student = Student('NJUST','4','ck','yuyuyu',18) # 这样就是继承
student.do_homework() # 可以用super找到父类的实例函数
# print(student.name)
# print(student.age)
# print(Student.sum)
# print(student.class_number)
# Student.do_homework(student) # 这个()内的参数甚至可以是“”只要是有东西就可以的，但是因为我在前面加了name所以一定要放一样的符合要求得内容才可以。
# Student.do_homework() 这个报错了
