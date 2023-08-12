a=float(input('Digite um número'))
b=float(input('Digite um número'))
c=float(input('Digite um número'))
if a>b+c or b>a+c or c>a+b:
    print('Não é um triângulo.')   
elif a==b and b==c and a==c:
    print('É um triângulo equilátero.')
elif a==b or b==c or c==a:
    print('É um triângulo isóceles.')
else:
    print('É um triângulo escaleno.')