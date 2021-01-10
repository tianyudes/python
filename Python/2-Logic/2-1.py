
account = 'tianyu'
password = '123456'

print('Please input the account')
user_account = input()
print('Please input the password')
user_password = input()
if user_account == account and user_password == password:
    print('success')
else:
    print('failure')

# python不存在常量

a = input()
a = int(a)
print(type(a), end='')
