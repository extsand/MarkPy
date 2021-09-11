welcome_msg = 'Hello, Mark! I glad to see you today'

print(welcome_msg)

def show_message(name, text='oops, I did not see text...'):
    print('======== message ===============')
    print(f'{name} say {text}')
    print('================================')

msg = ''
while msg != 'exit':

    msg = input('Enter your name: \n')
    text = input('Enter your text: \n')

    show_message(name=msg, text=text)




