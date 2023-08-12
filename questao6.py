num1=int(input('Digite o primeiro número: '))
num2=int(input('Digite o segundo número: '))
num3=int(input('DIgite o terceiro número: '))
if num1>num2 and num1>num3:
    if num1*num1==num2*num2+num3*num3:
        print('As informações formam um triângulo retângulo.')
    else: 
        print('As informações não formam um triângulo retângulo.')

elif num2>num1 and num2>num3:
    if num2*num2==num1*num1+num3*num3:
        print('As informações formam um triânuglo retângulo.')
    else:
        print('As informações não formam um triângulo retângulo.')
elif num3>num1 and num3>num2:
    if num3*num3==num1*num1+num2*num2:
        print('As informações formam um triângulo retângulo.')
    else:
        print('As informações não formam um triângulo retângulo.')