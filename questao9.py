grau=float(input('Digite em quantos graus a água se encontra: '))
if grau>100:
    print('A água está no estado gasoso')
elif grau<=0:
    print('A água está no estado sólido')

else:
    print('A água está no estado líquido')