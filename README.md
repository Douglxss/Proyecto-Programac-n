# ¿Qué es Python? #
En términos técnicos, Python es un lenguaje de programación de alto nivel, orientado a objetos, con una semántica dinámica integrada, principalmente para el desarrollo web y de aplicaciones informáticas.
Es muy atractivo en el campo del Desarrollo Rápido de Aplicaciones (RAD) porque ofrece tipificación dinámica y opciones de encuadernación dinámicas.
Python es relativamente simple, por lo que es fácil de aprender, ya que requiere una sintaxis única que se centra en la legibilidad. Los desarrolladores pueden leer y traducir el código Python mucho más fácilmente que otros lenguajes.
Por tanto, esto reduce el costo de mantenimiento y de desarrollo del programa porque permite que los equipos trabajen en colaboración sin barreras significativas de lenguaje y experimentación.
Además, soporta el uso de módulos y paquetes, lo que significa que los programas pueden ser diseñados en un estilo modular y el código puede ser reutilizado en varios proyectos. Una vez se ha desarrollado un módulo o paquete, se puede escalar para su uso en otros proyectos, y es fácil de importar o exportar.
Por otro lado, uno de los beneficios más importantes de Python es que tanto la librería estándar como el intérprete están disponibles gratuitamente, tanto en forma binaria como en forma de fuente.
Tampoco hay exclusividad, ya que Python y todas las herramientas necesarias están disponibles en todas las plataformas principales. Por lo tanto, es una opción multiplataforma, bastante tentadora para los desarrolladores que no quieren preocuparse por pagar altos costos de desarrollo.
En definitiva, es un lenguaje de programación relativamente fácil de aprender, y las herramientas necesarias están disponibles para todos de forma gratuita. Esto hace que sea accesible para casi todo el mundo. Si dispones de tiempo para aprender, conseguirás crear esos proyectos que tienes en mente.
# ¿Qué es una variable? #
Una variable es un sitio donde guardamos una determinada información. En función del tipo de información que guardemos (texto, números, booleanas, etc.), la variable será de uno u otro tipo. Por simplicidad sólo vamos a ver las variables de texto y numéricas, ya que son las que se usan en más del 80% de las ocasiones.
Cada variable debe tener un nombre con el que referirnos a ella. Python tiene en cuenta si escribimos en mayúsculas o minúsculas la variable (lo que se conoce como case sensitive). No es lo mismo una variable que se llame f1 que una que se llame F1.
Como es lógico y, para evitar confusiones, el nombre de la variable no puede coincidir con los nombres de los «comandos» de Python (if, for, etc.). Tampoco podremos usar nombres de variables con tildes o con ñ.
¿Y por qué hay que decir lo que se mete en cada variable? Porque en función de lo que haya dentro de ella, se podrán hacer una u otras cosas, como por ejemplo sumar dos números.
En Python estas son las variables más comunes:
## Números ##
En números hay dos tipos principales, los números enteros (llamados int) y los reales (llamados float). El separador decimal que tenemos que usar es el punto.
Aunque si no decimos el tipo de número que va a contener, Python intentará decidir por sí mismo cuál es el más apropiado, esto en ocasiones produce errores. Mi recomendación mientras estés empezando a aprender, es la de que siempre especificar qué tipo de número es, ya que evitará futuras frustraciones.
Definimos dos variables llamadas numero1 y # numero2, y asociaremos un número a cada una
número1=int (2)
número2=float (2.5)
print (número1)
2
print (número2)
2.5
Para saber de qué tipo es una determinada variable, basta con preguntarle a Python type(variable).

## Texto ##
Las variables que almacenan texto se denominan strings (str). Tienen que estar entre comillas sencillas (‘) o dobles («), o si el texto ocupa varias líneas, entre triples comillas dobles («»»).
Definimos dos variables llamadas texto y
texto2, y asociaremos un texto a cada una
texto="Esto es un texto"
texto2='Esto es otro texto'
print (texto)
Esto es un texto
print (texto2)
Esto es otro texto

Definimos una nueva variable texto3 que
incluye un texto multilínea.
texto3="""Hola
... caracola"""
print (texto3)
Hola
caracola

Al igual que sucedía con los números, Python supone que lo que introducimos es un texto al estar entre comillas, aunque siempre podemos forzarle a interpretarlo como texto usando el comando str.
texto3=str (54)
print(texto3)
54

Para unir dos textos, basta con usar el operador +.
## Print y variables ##
Como hemos visto, el comando print es de gran utilidad para que el programa pueda comunicarse con nosotros. Este comando muestra el texto que pongamos, o incluso el valor que hay dentro de una variable. En el caso de que juntemos texto y números, debemos tomar la precaución de convertir los números en texto, ya que si no, Python no sabe cómo se hace la suma de un texto y un número.
texto="Esto es un texto"
número=15

El siguiente comando devuelve un error
print (texto+" "+número)

Convirtiendo el número en texto, solucionamos el problema.
print (texto+" "+str(número))

## Operadores básicos ##
suma: +  
resta: -  
multiplicación: *  
división: /  
división entera: //  
módulo: %  
potenciación: **

### Suma 
``` python
#creamos dos variables para poder realizar la operación  
a = 2  
b = 5  
#creamos una variable donde almacenaremos nuestra operación  
result = 0  
#presentamos las dos variables acompañadas del operador suma  
result = (a + b)  
result = 7  
#presentamos un print para demostrar que nuestra operación sea correcta  
print (result)
```
### Resta 
``` python
#creamos dos variables para poder realizar la operación  
a = 2
b = 5  
#creamos una variable donde almacenaremos nuestra operación  
result = 0  
#presentamos las dos variables acompañadas del operador resta  
result = (a - b)  
result = -3  
#presentamos un print para demostrar que nuestra operación sea correcta  
print (result)
```
### Multiplicación
``` python
#creamos dos variables para poder realizar la operación  
a = 2 
b = 4  
#creamos una variable donde almacenaremos nuestra operación  
result = 0  
#presentamos las dos variables acompañadas del operador de multiplicación  
result = (a * b)  
result = 8    
#presentamos un print para demostrar que nuestra operación sea correcta  
print (result)
```

### División
``` python
#creamos dos variables para poder realizar la operación  
a = 4
b = 2  
#creamos una variable donde almacenaremos nuestra operación  
result = 0  
#presentamos las dos variables acompañadas del operador de división  
result = (a / b)  
result = 2 
#presentamos un print para demostrar que nuestra operación sea correcta  
print (result)
```

### Módulo
``` python
#creamos dos variables para poder realizar la operación  
a = 20  
b = 3  
#creamos una variable donde almacenaremos nuestra operación  
result = 0  
#presentamos las dos variables acompañadas del operador de módulo  
result = (a % b)  
result = 20  
#presentamos un print para demostrar que nuestra operación sea correcta  
print (result)
```
### Potencia 
``` python
#creamos dos variables para poder realizar la operación  
a = 2  
b = 2  
#creamos una variable donde almacenaremos nuestra operación  
result = 0  
#presentamos las dos variables acompañadas del operador de potencia  
result = (a ** b)  
result = 4  
#presentamos un print para demostrar que nuestra operación sea correcta  
print (result)
```
# Tipos de datos en Python 

## Integer
Los tipos enteros o int en Python permiten almacenar un valor numérico no decimal ya sea positivo o negativo de cualquier valor. La función type() nos devuelve el tipo de la variable, y podemos ver con efectivamente es de la clase int.
Ejemplos
``` python 
a = 0b100
b = 0x17
c = 0o720
print(a, type(a)) #4 <class 'int'>
print(b, type(b)) #23 <class 'int'>
print(c, type(c)) #464 <class 'int'>
```
## Float
El tipo numérico float permite representar un número positivo o negativo con decimales, es decir, números reales. Si vienes de otros lenguajes, tal vez conozcas el tipo doble, lo que significa que tiene el doble de precisión que un float. En Python las cosas son algo distintas, y los float son en realidad double.
Para saber más: Los valores float son almacenados de una forma muy particular, denominada representación en coma flotante. En el estándar IEEE 754 se explica con detalle.
Por lo tanto si declaramos una variable y le asignamos un valor decimal, por defecto la variable será de tipo float.
Ejemplo
``` python
f = 0.10093
print(f)       #0.10093
print(type(f)) #<class 'float'>


```



## String
Las cadenas en Python o strings son un tipo inmutable que permite almacenar secuencias de caracteres. Para crear una, es necesario incluir el texto entre comillas dobles ". Puedes obtener más ayuda con el comando help(str).
``` python
s = "Esto es una cadena"
print(s)       #Esto es una cadena
print(type(s)) #<class 'str'>
```
También es válido declarar las cadenas con comillas simples '.
``` python
s = 'Esto es otra cadena'
print(s)        #Esto es otra cadena
print(type(s))  #<class 'str'>
```
## Cast
Hacer un cast o casting significa convertir un tipo de dato a otro. Anteriormente hemos visto tipos como los int, string o float. Pues bien, es posible convertir de un tipo a otro.
Pero antes de nada, veamos los diferentes tipos de cast o conversión de tipos que se pueden hacer. Existen dos:
Conversión implícita: Es realizada automáticamente por Python. Sucede cuando realizamos ciertas operaciones con dos tipos distintos.
Conversión explícita: Es realizada expresamente por nosotros, como por ejemplo convertir de str a int con str().
Conversión implícita
Esta conversión de tipos es realizada automáticamente por Python, prácticamente sin que nos demos cuenta. Aun así, es importante saber lo que pasa por debajo para evitar problemas futuros.
El ejemplo más sencillo donde podemos ver este comportamiento es el siguiente:
``` python
a = 1   # <class 'int'>
b = 2.3 # <class 'float'>
a = a + b
print(a)       # 3.3
print(type(a)) # <class 'float'>
```
Conversión explicita
Por otro lado, podemos hacer conversiones entre tipos o cast de manera explícita haciendo uso de diferentes funciones que nos proporciona Python. Las más usadas son las siguientes:
float(), str(), int(), list(), set()
Y algunas otras como hex(), oct() y bin()

## List
Las listas en Python son uno de los tipos o estructuras de datos más versátiles del lenguaje, ya que permiten almacenar un conjunto arbitrario de datos. Es decir, podemos guardar en ellas prácticamente lo que sea. Si vienes de otros lenguajes de programación, se podría decir que son similares a los arrays.
``` python
lista = [1, 2, 3, 4]
```

## Tuple
Las tuplas en Python o tuples son muy similares a las listas, pero con dos diferencias. Son inmutables, lo que significa que no pueden ser modificadas una vez declaradas, y en vez de inicializarse con corchetes se hace con (). Dependiendo de lo que queramos hacer, las tuplas pueden ser más rápidas.
``` python 
tupla = (1, 2, 3)
print(tupla) #(1, 2, 3)
```
## Dictionary
Un diccionario en Python es una colección de elementos, donde cada uno tiene una llave key y un valor value. Los diccionarios se pueden crear con paréntesis {} separando con una coma cada par key: value. En el siguiente ejemplo tenemos tres keys que son el nombre, la edad y el documento.

``` python
d1 = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}
print(d1)
#{'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}
```
# Tomando decisiones 
## Sentencia If
De no ser por las estructuras de control, el código en cualquier lenguaje de programación sería ejecutado secuencialmente hasta terminar. Un código, no deja de ser un conjunto de instrucciones que son ejecutadas unas tras otra. Gracias a las estructuras de control, podemos cambiar el flujo de ejecución de un programa, haciendo que ciertos bloques de código se ejecuten si y solo si se dan unas condiciones particulares.
Uso del if
Un ejemplo sería si tenemos dos valores a y b que queremos dividir. Antes de entrar en el bloque de código que divide a/b, sería importante verificar que b es distinto de cero, ya que la división por cero no está definida. Es aquí donde entran los condicionales if.
``` python
a = 4
b = 2
if b != 0:
    print(a/b)
```
## Ciclo for
A continuación explicaremos el bucle for y sus particularidades en Python, que comparado con otros lenguajes de comparación, tiene ciertas diferencias.
El for es un tipo de bucle, parecido al while pero con ciertas diferencias. La principal es que el número de iteraciones de un for está definido de antemano, mientras que en un while no. La diferencia principal con respecto al while es en la condición. Mientras que en el while la condición era evaluada en cada iteración para decidir si volver a ejecutar o no el código, en el for no existe tal condición, sino un iterable que define las veces que se ejecutará el código. En el siguiente ejemplo vemos un bucle for que se ejecuta 5 veces, y donde la i incrementa su valor “automáticamente” en 1 en cada iteración.
``` python 
for i in range(0, 5):
    print(i)

# Salida:
# 0
# 1
# 2
# 3
# 4
```
## Ciclo While
El uso del while nos permite ejecutar una sección de código repetidas veces, de ahí su nombre. El código se ejecutará mientras una condición determinada se cumpla. Cuando se deje de cumplir, se saldrá del bucle y se continuará la ejecución normal. Llamaremos iteración a una ejecución completa del bloque de código.
Cabe destacar que existe dos tipos de bucles, los que tienen un número de iteraciones no definidas, y los que tienen un número de iteraciones definidas. El while estaría dentro del primer tipo. Mas adelante veremos los for, que se engloban en el segundo.
``` python 
x = 5
while x > 0:
    x -=1
    print(x)

# Salida: 4,3,2,1,0
```
## Break
#### Break con bucles for
Veamos cómo podemos usar el break con bucles for. El range(5) generaría 5 iteraciones, donde la i valdría de 0 a 4. Sin embargo, en la primera iteración, terminamos el bucle prematuramente.
El break hace que nada más empezar el bucle, se rompa y se salga sin haber hecho nada.
``` python
for i in range(5):
    print(i)
    break
    # No llega

# Salida: 0
```
Un ejemplo un poco más útil, sería el de buscar una letra en una palabra. Se itera toda la palabra y en el momento en el que se encuentra la letra que buscábamos, se rompe el bucle y se sale.
Esto es algo muy útil porque si ya encontramos lo que estábamos buscando, no tendría mucho sentido seguir iterando la lista, ya que desperdiciaríamos recursos.
``` python
cadena = 'Python'
for letra in cadena:
    if letra == 'h':
        print("Se encontró la h")
        break
    print(letra)

# Salida:
# P
# y
# t
# Se encontró la h
```
#### Break con bucles while
El break también nos permite alterar el comportamiento del while. Veamos un ejemplo.
La condición while True haría que la sección de código se ejecutara indefinidamente, pero al hacer uso del break, el bucle se romperá cuando x valga cero.
``` python
x = 5
while True:
    x -= 1
    print(x)
    if x == 0:
        break
    print("Fin del bucle")

#4, 3, 2, 1, 0
```
Por norma general, y salvo casos muy concretos, si ves un while True, es probable que haya un break dentro del bucle.
#### Break y bucles anidados
Como hemos dicho, el uso de break rompe el bucle, pero sólo aquel en el que está dentro.
Es decir, si tenemos dos bucles anidados, el break romperá el bucle anidado, pero no el exterior.
``` python
for i in range(0, 4):
    for j in range(0, 4):
        break
        #Nunca se realiza más de una iteración
    # El break no afecta a este for
    print(i, j)

# 0 0
# 1 0
# 2 0
# 3 0
```
## Continue

El uso de continue al igual que el ya visto break, nos permite modificar el comportamiento de de los bucles while y for.
Concretamente, continue se salta todo el código restante en la iteración actual y vuelve al principio en el caso de que aún queden iteraciones por completar.
La diferencia entre el break y continue es que el continue no rompe el bucle, si no que pasa a la siguiente iteración saltando el código pendiente.
En el siguiente ejemplo vemos como al encontrar la letra P se llama al continue, lo que hace que se salte el print(). Es por ello por lo que no vemos la letra P impresa en pantalla.
``` python
cadena = 'Python'
for letra in cadena:
    if letra == 'P':
        continue
    print(letra)
# Salida:
# y
# t
# h
# o
# n
```

