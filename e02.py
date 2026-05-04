from random import randint
n2=randint(1,20)
n1=0
c=6
intentos=7
print('Trate de adivinar el numero del 1 al 20')
print('Tiene 6 intentos')
print('')

for x in range(1,intentos,1):
    print('Ingrese un numero')
    n1=int(input())
    if (n1==n2):
        print('Numero correcto, es el',n1)
        break
    else:
        if (n1>n2):
            print('El numero es mas bajo')
            c=c-1
            print('Perdiste un intento, te quedan ',c,' intentos')
            print('')
        else:
            print('El numero es mas alto')
            c=c-1
            print('Perdiste un intento, te quedan ',c,' intentos')
            print('')
            
if (n1!=n2):           
    print('Te quedaste sin intentos, el número era ',n2)
