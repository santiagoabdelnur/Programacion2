import math

r=0
h=0

def area_circulo(r):
    if(r<0):
        print("El radio del circulo no puede ser negativo")
        return 
    area_circulo=math.pi*(r**2)
    return area_circulo

print("Ingrese el radio del circulo")
r=int(input())

resultdo=0
resultado = area_circulo(r)

def volumen_cilindro(r, h):
    volumen_cilindro=area_circulo(r)
    volumen=volumen_cilindro*h
    return volumen


print("Ingrese la altura del cilindro")
h=int(input())

resultado_volumen=0
resultado_volumen=volumen_cilindro(r, h)

print("El volumen del cilindro es: ",int(resultado_volumen))
print("El área del circulo es: ",int(resultado))
