print("hola, mundo")
a=5
b=6
print("la suma es: ",a+b)



# Función para sumar dos números
def suma(a, b):
    return a + b

# Función para restar dos números
def resta(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicacion(a, b):
    return a * b

# Función para dividir dos números
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero."

print("¡Hola, mundo!")
print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Solicitar al usuario que elija una operación
opcion = input("Seleccione una operación (1/2/3/4): ")

# Solicitar al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if opcion == '1':
    print("La suma es:", suma(num1, num2))
elif opcion == '2':
    print("La resta es:", resta(num1, num2))
elif opcion == '3':
    print("La multiplicación es:", multiplicacion(num1, num2))
elif opcion == '4':
    print("La división es:", division(num1, num2))
else:
    print("Opción no válida")

