# ¿Qué es Python? #
En términos técnicos, Python es un lenguaje de programación de alto nivel, orientado a objetos, con una semántica dinámica integrada, principalmente para el desarrollo web y de aplicaciones informáticas.
Es muy atractivo en el campo del Desarrollo Rápido de Aplicaciones (RAD) porque ofrece tipificación dinámica y opciones de encuadernación dinámicas.
Python es relativamente simple, por lo que es fácil de aprender, ya que requiere una sintaxis única que se centra en la legibilidad. Los desarrolladores pueden leer y traducir el código Python mucho más fácilmente que otros lenguajes.
Por tanto, esto reduce el costo de mantenimiento y de desarrollo del programa porque permite que los equipos trabajen en colaboración sin barreras significativas de lenguaje y experimentación.
Además, soporta el uso de módulos y paquetes, lo que significa que los programas pueden ser diseñados en un estilo modular y el código puede ser reutilizado en varios proyectos. Una vez se ha desarrollado un módulo o paquete, se puede escalar para su uso en otros proyectos, y es fácil de importar o exportar.
Por otro lado, uno de los beneficios más importantes de Python es que tanto la librería estándar como el intérprete están disponibles gratuitamente, tanto en forma binaria como en forma de fuente.
Tampoco hay exclusividad, ya que Python y todas las herramientas necesarias están disponibles en todas las plataformas principales. Por lo tanto, es una opción multiplataforma, bastante tentadora para los desarrolladores que no quieren preocuparse por pagar altos costos de desarrollo.
En definitiva, es un lenguaje de programación relativamente fácil de aprender, y las herramientas necesarias están disponibles para todos de forma gratuita. Esto hace que sea accesible para casi todo el mundo. Si dispones de tiempo para aprender, conseguirás crear esos proyectos que tienes en mente.
# Tipos de variables en Python #
Una variable es un sitio donde guardamos una determinada información. En función del tipo de información que guardemos (texto, números, booleanas, etc.), la variable será de uno u otro tipo. Por simplicidad sólo vamos a ver las variables de texto y numéricas, ya que son las que se usan en más del 80% de las ocasiones.
Cada variable debe tener un nombre con el que referirnos a ella. Python tiene en cuenta si escribimos en mayúsculas o minúsculas la variable (lo que se conoce como case sensitive). No es lo mismo una variable que se llame f1 que una que se llame F1.
Como es lógico y, para evitar confusiones, el nombre de la variable no puede coincidir con los nombres de los «comandos» de Python (if, for, etc.). Tampoco podremos usar nombres de variables con tildes o con ñ.
¿Y por qué hay que decir lo que se mete en cada variable? Porque en función de lo que haya dentro de ella, se podrán hacer una u otras cosas, como por ejemplo sumar dos números.
En Python estas son las variables más comunes:
# Números #
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

# Texto #
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
# Print y variables #
Como hemos visto, el comando print es de gran utilidad para que el programa pueda comunicarse con nosotros. Este comando muestra el texto que pongamos, o incluso el valor que hay dentro de una variable. En el caso de que juntemos texto y números, debemos tomar la precaución de convertir los números en texto, ya que si no, Python no sabe cómo se hace la suma de un texto y un número.
texto="Esto es un texto"
número=15

El siguiente comando devuelve un error
print (texto+" "+número)

Convirtiendo el número en texto, solucionamos el problema.
print (texto+" "+str(número))

# Operadores básicos #
suma: +  
resta: -  
multiplicación: *  
división: /  
división entera: //  
módulo: %  
potenciación: **

# Suma #
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
#Resta 
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

#Multiplicación 
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


#División 
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

#Módulo 
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

#Potencia 
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

