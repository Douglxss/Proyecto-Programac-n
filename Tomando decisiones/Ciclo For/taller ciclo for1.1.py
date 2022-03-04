n= int(input("Ingrese el valor N: "))
suma=0
for i in range(n):
    nota=int(input("Ingrese su calificación: "))
    suma= suma+nota

print("Suma total: ", suma)
promedio =suma/n
print("El promedio es:", promedio)

