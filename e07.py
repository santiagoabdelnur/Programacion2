import datetime

#Solicitar datos al usuario
d = int(input("Ingresa tu dia de nacimiento : "))
m = int(input("Ingresa tu mes de nacimiento : "))
a = int(input("Ingresa tu año de nacimiento : "))

#Crear fecha de nacimiento y obtener la fecha actual
fn = datetime.datetime(a, m, d)
fa = datetime.datetime.now()

t_delta = fa - fn
dt = t_delta.days

#Calcular años y meses 
a = dt // 365
dr = dt % 365
m = dr // 30

ts = fn.timestamp()

print("Fecha de nacimiento:", fn.strftime("%d/%m/%Y"))
print("Total de segundos:", int(ts))
print("Dias totales:", dt)
print("Meses totales:", m)
print("Edad:", a, "años")
