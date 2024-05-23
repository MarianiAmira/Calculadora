from os import system

def calculadora()-> str:
    print("a. Ingresar primero operando: ")
    print("b. Ingresar segundo operando: ")
    print("c. Elegir operacion: ")
    print("d. Mostrar resultado: ")
    print("e. Salir")

    opcion = input("Ingrese la opcion: ")

    return opcion

def ingresar_primero_operador():
    primer_operando = int(input("Ingrese el primero operando: "))
    return primer_operando

def ingresar_segundo_operador():
    segundo_operando = int(input("Ingrese el segundo operando: "))
    return segundo_operando

def mensaje_opciones_operaciones():
    opciones_operaciones = print("\nOperaciones para elegir:\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n")

    return opciones_operaciones

def operacion_elegida(a:int, b:int)->int:
    operacion_elegida = input("Eliga la operacion que desea: ")
    match operacion_elegida:
        case "1":
            resultado = a + b
        case "2":
            resultado = a - b
        case "3":
            resultado = a * b
        case "4":
            resultado = a / b
    
    return resultado

def mostrar_resultado(resultado):
    mensaje = print(resultado)
    return mensaje

def pedir_confirmacion(mensaje:str)->bool:
    rta = input(mensaje).lower()
    return rta == 's'

def pausar():
    system("pause")

def limpiar_pantalla():
    system("cls")