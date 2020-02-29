# Autor: José Manuel Rivera Sosapavón
# Descripcion: Cuenta.

# Escribe tu programa después de esta línea.

c = float(input("Teclea el precio de tu comida: "))

p = c*.13
i = c*.16
t = c+p+i

print("subtotal: ",c)
print("propina: ",p)
print("IVA: ",i)
print("total: ",t)