def cifrado_cesar(mensaje, codigo):
    rdo = ""
    desplazamiento = list(mensaje)
    for i in range(len(desplazamiento)):
        if desplazamiento[i].isspace(): 
            rdo += desplazamiento[i]
        elif desplazamiento[i].isupper(): 
            rdo += chr((ord(desplazamiento[i]) + codigo - 65) % 26 + 65)
        elif desplazamiento[i].islower():
            rdo += chr((ord(desplazamiento[i]) + codigo - 97) % 26 + 97)
        else: 
            rdo += desplazamiento[i]
    return rdo

mensaje = input("Ingrese el mensaje que quiera descifrar: ")
codigo = int(input("Ingrese de cuanto se desplaza: "))
print(cifrado_cesar(mensaje, codigo))