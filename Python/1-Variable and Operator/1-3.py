# 列表的可变和元组的不可变

a = 3 / 2
# 1.5
a = 3 // 2
# 1
c = 3 % 2
# 1
d = 2 ** 5
# 32

# 元组和列表也可以比较


print(1 and 0)
print(1 or 0)
print('a' and 'b')

a = 1
print(a in [1, 2, 3, 4])
# True


# Difference between "==" and  "is"
a = 787878
b = 787878
print(1 == 1.0)
print(1 is 1.0)
print('----------------')
print(a is b)
'''
== depends on the value
is compares the id 
a = {1,2,3} b = {2,1,3}
a == b -> True               a is b -> False 

c = (1,2,3) d = (2,1,3)
c == d False 
c is d False


Obtain the type of the object. 
1. type(a) == int  cannot used to judge the subtype.
2. isinstance(a, int)
    2.1 isinstance(a,(int, str, float)) 
    
Three feature of the object： id value type
'''

