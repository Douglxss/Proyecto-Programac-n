op = -1
while op != 0:
    print("<1>Sumar")
    print("<2>Restar")
    print("<3>Multiplicar")
    print("<4>Dividir")
    op = int(input("Ingrese que operacion va a usar"))
    if op != 0 :
        num1 = int(input("Ingrese Primer Numero"))
        num2 = int(input("Ingrese Segundn Numero"))
    if op == 1:
        print("suma=", num1 + num2)
    elif op == 2:
        print("Resta=", num1 - num2)
    elif op == 3:
        print("Multiplicacion=", num1 * num2)
    elif op == 4:
        print("Division=", num1 / num2)
    else:
        print("No existe la Opcion")

