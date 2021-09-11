welcome_msg = 'Hello, Mark! I glad to see you today'

print(welcome_msg)

def showName(name, text):
    print('======== message ===============')
    print(f'{name} say {text}')
    print('================================')


name = ''
while name != 'exit':
    name = input('Enter your Name: \n')
    msg = input('Enter your Text: \n')
    showName(name=name, text=msg)


