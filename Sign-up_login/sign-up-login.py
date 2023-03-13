print('Create an account here: ' )

username = input('Enter username: ')
password = input('Enter password')

print('Your account has succesfull been created')
print('log-in here: ')

username2 = input("Enter username: ")
password2 = input('Enter password ')

if username == username2 and password == password2:
    print('you have succefully logged in :) ')
else:
    print('invalid credentials')
