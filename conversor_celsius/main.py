def fah(celsius):
  conversao = (celsius * 1.8)+32
  return print('Fahrenheit', conversao)
  
def kelvin(celsius):
  conversao = celsius + 273.15
  return print('Kelvin', conversao)

def newton(celsius):
  conversao = celsius / 3.03030303
  return print('Newton', conversao)

print('Digite valor em celsius')
celsiu = float(input())
print('''
1 Fahrenheit
2 Kelvin
3 Newton
''')
print('Digite a conversão desejada')
menu = input()

if menu == '1':
  fah(celsiu)
elif menu == '2':
  kelvin(celsiu)
elif menu == '3':
  newton(celsiu)
else:
  print('Opção invalida!!!')