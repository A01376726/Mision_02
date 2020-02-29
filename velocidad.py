# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Velocidad
# Escribe tu programa después de esta línea.

# La velocidad de un auto puede calcularse con la fórmula v = d/t.
#(v-velocidad, d-distancia, t-tiempo).
#Elabora un algoritmo y escribe un programa que pregunte al usuario la velocidad a la que viaja un auto (km/h, número entero)
#y calcule e imprima lo siguiente:
#	La distancia en km. que recorre en 6 hrs.
#•	La distancia en km. que recorre en 3.5 hrs.
#•	El tiempo en horas que requiere para recorrer 485 km.

v = float(input("Teclea la velocidad en km/hr :"))

distancia = 6*v
d = 3.5*v
t = 485/v

print("distancia: %.2f km" % (distancia))
print("distancia:%.2f km"% (d))                        
print("tiempo: %.2f hrs" % (t))