
a = [1, 2, 3]
print(id(a))
a[0] = 1
print(id(a))
# The output of the id remains the same.

a = (1, 2, 3)
# a[0] = 1, There will be an error.


b = [1, 2, 3, 4]
b.append(7)
print(b)

# From the example above, obviously, list is more useful than the tuple, but in the mass system, there are many
# developer, tuple can make sure the important data will not be rewrite.
# SO IN THE DEVELPOMENT, TUPLE GOES FIRST

c = (1, 2, 3, [1, 23, 4])

c[3][2] = 5
print(c[3][2])

# output: 5

