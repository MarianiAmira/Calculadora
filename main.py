from calculadora import *

flag_primer_numero = False
flag_segundo_numero = False
flag_operacion = False
seguir = "s"

while seguir ==  "s":
    match calculadora():
        case "a":
            primer_operando = ingresar_primero_operador()
            flag_primer_numero = True
        case "b":
            if flag_primer_numero:
                segundo_operando = ingresar_segundo_operador()
                flag_segundo_numero = True
            else:
                print("Primero tiene que ingresar el primer operando...")
        case "c":
            if not flag_primer_numero and not flag_segundo_numero:
                print("Primero tiene que ingresar el primer y segundo operando...")
            elif not flag_segundo_numero :
                print("Debe ingresar primero el segundo operador...")
            else:
                mensaje_opciones_operaciones()
                resultado = operacion_elegida(primer_operando, segundo_operando)
                flag_operacion = True

            '''if flag_primer_numero and flag_segundo_numero:
                mensaje_opciones_operaciones()
                resultado = operacion_elegida(primer_operando, segundo_operando)
                flag_operacion = True
            else:
                print("Primero tiene que ingresar el primer y segundo operando...")'''
        case "d":
            if flag_primer_numero and flag_segundo_numero and flag_operacion:
                mostrar_resultado(resultado)
            else:
               print("Primero tiene que ingresar el primer, el segundo operando y elegir la opracion que desea...") 
        case "e":
            if pedir_confirmacion("Confirma salida? s/n: "):
                seguir = "n"
            continue

    pausar()

print("Fin de programa")