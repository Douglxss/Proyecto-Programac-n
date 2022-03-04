#pedir al usuario un valor. Si el valor el positivo, 
#pedir un segundo valor y calcular la suma, resta y producto de ambos
#Mostrar los Resultados por Pantalla

num1 = int(input("Ingrese Primer numero"))
if num1>0:
    num2= int(input("ingrese Segundo numero"))
    suma = num1 + num2
    print(num1, "+", num2, "=", suma)

    resta = num1 - num2
    print(num1, "-", num2, "=", resta)

    multiplicacion = num1 * num2
    print(num1, "*", num2, "=", multiplicacion)
else:
    print("el numero que inserto es negativo")


