# Autor: José Manuel Rivera Sosapavón
# Descripcion: Clase

# Escribe tu programa después de esta línea.

h = int(input ("Alumnos hombres: "))
m = int(input("Alumnas mujeres: "))

t = m+h
ph = 100/t*h

pm = 100/t*m

print("Total de inscritos: ",t)
print("Porcentaje de mujeres en la clase: %.2f" %(pm))
print("Porjentaje de mujeres en la clase:%.2f " %(ph))
        