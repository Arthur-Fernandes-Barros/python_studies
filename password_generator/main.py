import random 

print('Bem-vindo ao gerador de senhas')

chars = 'asdfghjklçzxcvbnmqwertyuiopASDFGHJKLÇQWERTYUIOPZXCVBNM!@#$%¨&*()1234567890'

number = int(input('Quantas senhas?'))

length = int(input('Qual o tamanho da senha'))

print('\naqui estão as suas senhas')
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars) 
    print(passwords)