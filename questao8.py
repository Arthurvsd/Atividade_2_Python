forma=int(input('Escolha uma forma geométrica: 1 - Retângulo, 2 - Triângulo, 3 - Círculo'))
if forma==1:
    base=float(input('Qual a base? '))
    altura=float(input('Qual a altura? '))
    print(base*altura)
elif forma==2:
    base=float(input('Qual a base? '))
    altura=float(input('Qual a altura? '))
    print(base*altura/2)
else:
    raio=float(input('Qual o raio? '))
    print(3.14*raio*raio)