#Dada la fecha de hoy
#Cacular la fecha del día siguiente 
#suponiendo que el año no es bisiesto

di=0
me=0
an=0

s_d=0
s_m=0
s_a=0

m31= (1,3,5,7,8,10,12)
m30= (4,6,9,11)

while True: 
    print("Ingresa una fecha ")
    print("Ingresar día", end = " ")
    di = int(input())
    print("Ingresar mes", end = " ")
    me = int(input())
    print("Ingresar año", end = " ")
    an = int(input())
    s_d = di+1
    s_m = me
    s_a = an
    if me == 12 and di == 31:
        s_d == 1
        s_m == 1
        s_a == an+1
    else:
        s_a == an
    for i in range(len(m31)):
        if di == 31 and me == m31[i]:
            s_d == 1
            s_m == me+1 

    for i in range(len(m30)):
        if di == 30 and me == m30[i]:
            s_d == 1
            s_m == me+1 
    if me == 2 and di == 28: 
        s_d == 1
        s_m == me + 1
    leap_year = an % 4
    if di == 29 and me== 2 and leap_year == 0:
        s_d == 1 
        s_m == me + 1
    if di >= 32 and me >= 13: 
        print("Fecha incorrecta, favor ingresar una fecha real")
    else:
        print("Día ingresado:",di,"/",me,"/",an)    
        print("Siguiente día:",s_d,"/",s_m,"/",s_a)
           