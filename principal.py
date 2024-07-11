from funciones import *
os.system("cls")
print("Bienvenido al programa generador y asignador de sueldos!")
while True:
    print(">>Presione un tecla para continuar<<")
    msvcrt.getch()
    os.system("cls")
    print("\tMENÚ\n")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    opc=input("Ingrese un número del menú: ")
    os.system("cls")
    if opc=="1":
        opc_1()
    elif opc=="2":
        opc_2()
    elif opc=="3":
        opc_3()
    elif opc=="4":
        opc_4()
    elif opc=="5":
        opc_5()
    else:
        print("Error! Debe ingresar un número del 1 al 5!")