def celsius_a_fahrenheit(temp_c):
    temp_f=(temp_c*1.8)+32
    return temp_f

def fahrenheit_a_celsius(temp_f):
    temp_c=(temp_f-32)/1.8
    return temp_c

temp_c=0
temp_c=int(input("Ingrese una temperatura en°C: "))

temp_f=celsius_a_fahrenheit(temp_c)
print(temp_c,"°C equivalen a ",temp_f,"°F")

temp_f2=0
temp_f2=int(input("Ingrese una temperatura en°F: "))
temp_c2 = fahrenheit_a_celsius(temp_f2)

print(temp_f2,"°F equivalen a ",temp_c2,"°C")
