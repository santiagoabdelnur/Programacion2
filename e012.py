import random
estudiantes = ["Tomas", "Ismael", "León", "Santiago",]
orden_exposicion = []
for i in range(len(estudiantes)):
    aleatorio = random.randint(0, len(estudiantes) - 1)
    orden_exposicion.append(estudiantes.pop(aleatorio))
    
print("El orden a exponer es:")
for i in range(len(orden_exposicion)):
    print(f"{i + 1}. {orden_exposicion[i]}")