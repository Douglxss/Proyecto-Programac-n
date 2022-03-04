from sys import maxsize


n = 5
suma = 0
menor = maxsize

for i in range(n):
    num = int(input("Ingrese numero "))
    suma += num
    if num < menor:
        menor = num
print("Promedio", suma/n)
print("Menor", menor)
