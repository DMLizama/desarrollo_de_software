import sys

def suma(n1,n2):
    result = str(n1 + n2)
    print("El resultado es "+result)

def resta(n1,n2):
    result = n1 - n2#str(n1 - n2)
    print(f"El resultado es {result}") #con uso de fstring o formatString

def multiplicacion(n1,n2):
    result = str(n1 * n2)
    print("El resultado es "+result)

def division(n1,n2):
    result = str(n1/n2)
    print("El resultado es "+result)

operacion = sys.argv[1]
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

match operacion:
    case "suma":
        suma(n1,n2)
    case "resta":
        resta(n1,n2)
    case "multiplicacion":
        multiplicacion(n1,n2)
    case "division":
        division(n1,n2)
    case _:
        print("operación inválida...")