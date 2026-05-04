n=0
dn=0
xn=0
bn=0

print('Conversor Decimal-Binario-Hexadecimal')
#print('Ingrese 1 para convertir un numero decimal a hexadecimal o binario')
#print('Ingrese 2 para convertir un numero binario a hexadecimal o decimal')
#print('Ingrese 3 para convertir un numero hexadecimal a decimal o binario')

n=int(input())

#if(n==1):
print('Ingrese un numero decimal')
dn=int(input())
    
xn=hex(dn)
print(dn,' en hexadecimal es ',xn)
    
bn=bin(dn)
print(dn,' en binario es ',bn)
