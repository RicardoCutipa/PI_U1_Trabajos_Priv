
def ejercicio1(): 
    capital = float(input("Ingrese el capital a invertir: "))
    Interes = capital*0.02
    print("La ganancia obtenida es: ", Interes)


def ejercicio2():
    Sueldo = float(input("Ingrese el sueldo base: "))
    comision1 = float(input("Ingrese la cantidad obtenida en la primera venta: "))
    comision2 = float(input("Ingrese la cantidad obtenida en la segunda venta: "))
    comision3 = float(input("Ingrese la cantidad obtenida en la tercera venta: "))
    comisionSuma = comision1 + comision2 +comision3
    comision_Final = comisionSuma*0.1
    print("Sueldo Total: ", Sueldo+comision_Final)
    print("Comision Total: ", comision_Final)

def ejercicio3():
    precioCompra = float(input("Ingrese el precio: "))
    Descuento = precioCompra * 0.15
    PrecioFinal = precioCompra - Descuento
    print("El precio a pagar es: ", PrecioFinal)

def ejercicio4():
    print("Ingrese las notas de los examenes Parciales")
    Nota1 = int(input("Nota 01: "))
    Nota2 = int(input("Nota 02: "))
    Nota3 = int(input("Nota 03: "))
    ParcialPorcentaje = float((Nota1 + Nota2 +Nota3)*0.55)

    print("Nota Examen Final")
    NotaEF = int(input("Ingrese la nota de Examen Final: "))
    NotaEFPorcentaje = float(NotaEF*0.30)

    print("Nota del Trabajo Final")
    NotaTF = int(input("Nota Trabajo Final: "))
    NotaTFPorcentaje = float(NotaTF*0.15)

    print("Calificacion Final: ",ParcialPorcentaje + NotaEFPorcentaje + NotaTFPorcentaje)


def ejercicio5():
    print("Porcentaje de Hombres y Mujeres")
    Hombres = int(input("Ingrese la cantidad de Hombres: "))
    Mujeres = int(input("Ingrese la cantidad de Mujeres: "))
    TotalMH = int(Hombres + Mujeres)

    PorcentajeH = float(float(Hombres*100)/TotalMH)
    PorcentajeM = float(float(Mujeres*100)/TotalMH)

    print("Cantidad de Alumnos: ",TotalMH)
    print("Porcentaje de Hombres: ",PorcentajeH,"%")
    print("Porcentaje de Mujeres: ",PorcentajeM,"%")


def ejercicio6():
    Anio = int(input("Ingrese su año de nacimiento: "))
    Edad = 2022 - Anio
    print("Su edad actual es: ",Edad)


# Ejecutar ejercicios
# ejercicio1()
# ejercicio2()
# ejercicio3()
# ejercicio4()
# ejercicio5()
# ejercicio6()
