caram = 0
estud = 0
cxalum = 0

print ("¿cuantos estudiantes hay en el curso?")
estud = int(input())

print("¿Cuantos caramelos tengo?")
caram = int(input())

cxalum = caram // estud
print ("El numero de caramelos que recibe cada alumno es de ",cxalum)

crest = caram % estud
print ("Quedaron un total de ",crest," caramelos")

