import os, time, msvcrt, random, csv
trabajadores=["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos=[]
def opc_1():
    print("\tASIGNAR SUELDOS ALEATORIOS\n")
    opc_sueldo=1
    if len(sueldos)==10:
        while True:
            try:
                opc_sueldo=int(input(("Ya existen sueldos asignados a trabajadores, ¿desea volver a asignarles un sueldo aleatorio? (1: sí - 2: no)")))
                if opc_sueldo in(1,2):
                    break
                else:
                    print("Error! Debe ingresar un 1 para sí o un 2 para no!")
            except:
                print("Error! Debe ingresar un número entero")
    if opc_sueldo==1:
        sueldos.clear()
        for x in range(len(trabajadores)):
            sueldo_aleatorio=random.randint(300000,2500000)
            sueldos.append(sueldo_aleatorio)
        print("Los sueldos se han asiganado exitosamente!")
        print (sueldos)
    else:
        print("No se han modificado los sueldos asignados.")