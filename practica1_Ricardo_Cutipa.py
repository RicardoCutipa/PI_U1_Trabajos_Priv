# a = input("Ingrese su nombre: ")
# b = input("Ingrese su apellido: ")
# d = int(input("Ingrese un numero: "))
# e = float(input("Ingrese un decimal: "))
# c = a+b
# resultado =d*e
# print("Hola "+c)
# print("El valor de la multiplicacion es: ",resultado)
# print("El valor de la potencia es: ",3**4)
# print("---------------------------------------------")
# num1 =float(input("Ingrese el numero: "))
# elevado = int(input("Ingrese la potencia: "))
# NumeroF=num1*elevado

# NumeroF =float(input("El resultado es: "))


# Ejercicio 1
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
Sumanumero12 = int(numero1 + numero2)
print("El resultado de la suma da: ",Sumanumero12)


# Ejercicio 2
print("Ingrese las notas: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 =float(input("Nota 3: "))
nota4 = float (input("Nota 4: "))
NotaFinal = float(float(nota1+nota2+nota3+nota4)/float(4))
print("Promedio Final: ",NotaFinal)

# Ejercicio 3
print("Area del Rectangulo")
basee = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
AreaRec = float(basee*altura)
print("El area es: ",AreaRec)

# Ejercicio 4
print("Area del Circulo")
radio = float(input("Ingrese el radio: "))
pi = 3.14
radio2 = radio*radio
AreaCi = float(pi*radio2)
print("El Area del Circulo es: ",AreaCi)

# Ejercicio 5
A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))
C = float(input("Ingrese el valor de C: "))

AreaRecgg = float(B*C)
AreaTrian = float(float(B*(A-C))/float(2))

AreaTotal = float(AreaRecgg + AreaTrian)
print("----------------------------")
print("El Area Total es: ",AreaTotal)
print("Area del Triangulo: ",AreaTrian)
print("Area del Rectangulo: ",AreaRecgg)
