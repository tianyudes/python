
A =[1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(A)
# Use the simple word to represent the variable.
# Attention to the the capital letter


a = 1
# a->1
b = a
# b -> 1
a = 3
# a -> 3，but b->1
print(b)  # Here the result should be 1.

a = [1, 2, 3, 4]
b = a
a[0] = '1'
print(b) # Output is [1, 2, 3, 4]
'''
int str tuple are value types，list，dic set are reference type.
The value of the value type is invariable, but the reference type is variable. 
'''

b = 'python'
print(id(b))
b = b + 'hello'
print(id(b))

# The output of the id is not the same, which means a new variable called b is created.
# The same with the int and tuple type.

# 'python'[0] = 'o' False



