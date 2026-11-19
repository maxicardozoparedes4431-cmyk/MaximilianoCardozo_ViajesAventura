from persistencia.crear_bd import crear_tablas
from persistencia.semilla_bd import cargar_datos
from time import sleep
from menus.menu_sesion import solicitar_login
import subprocess
import random

def cls():
    subprocess.run("cls", shell=True)
    sleep(random.choice([1, 1.2, 1.5, 2]))

#crear_tablas()
#cargar_datos()

while True:

    while True: # menu de inicio de sesion
        cls()
        print("---- INICIO DE SESIÓN ----")
        print("1. Iniciar Sesión")
        print("2. Salir")

        opcioninicio = input("Seleccione una opcion: ")

        try:
            if opcioninicio.isdigit():
                print(opcioninicio)
        except ValueError:
            print("Ingrese un valor de 1 al 3")

        if opcioninicio == "1":
            cls()
            usuario = solicitar_login()
            if usuario is not None:
                break
        elif opcioninicio == "2":
            break
        else:
            input("Opcion invalida, por favor seleccione una opcion del 1 al 2")

    try:
        if usuario.rol == "admin":
            usuario = None
        else:
            usuario = None            

    except Exception:
        print("Saliendo del programa...")
        break