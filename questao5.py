nulos=int(input('Quantos votos nulos tiveram? '))
branco=int(input('Quantos em branco? '))
naruto=int(input('Quantos votos o Naruto obteve? '))
sakura=int (input('Quantos votos a Sakura obteve? '))
shin=int (input('Quantos votos Shin obteve? '))
if naruto+sakura+shin>branco+nulos:
    print('A votação foi válida!')
    if naruto>sakura and naruto>shin:
        print('Naruto ganhou a eleição!')
    if sakura>naruto and sakura>shin:
        print('Sakura ganhou a eleição!')
    if shin>naruto and shin>sakura:
        print('Shin ganhou a eleição!')
else:
    print('A eleição não foi válida!')