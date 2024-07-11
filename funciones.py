import os, time, msvcrt, random, csv
trabajadores=["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos=[]
trabajadores_con_sueldos:[]
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

def opc_2():
    if not sueldos:
        print("Error! Primero debe asignarle un sueldo a los trabajadores!")
    else:
        print("\tCLASIFICAR SUELDOS\n")
        menor_800=0
        entre_800_y_2=0
        mayor_2=0
        t_menor_800=[]
        t_entre_800_y_2=[]
        t_mayor_2=[]
        for s in sueldos:
            if s<=800000:
                menor_800+=1
                t_menor_800.append(sueldos.index(s))
            elif s>800000 and s<=2000000:
                entre_800_y_2+=1
                t_entre_800_y_2.append(sueldos.index(s))
            else:
                mayor_2+=1
                t_mayor_2.append(sueldos.index(s))
        print(f"Sueldos menores a $800.000 TOTAL: {menor_800}\n")
        print("Nombre empleado\t\tSueldo")
        for x in t_menor_800:
            print(f"{trabajadores[x]}\t\t${sueldos[x]}")
        print("\nSueldos entre $800.000 y $2.000.000")
        print(f"TOTAL: {entre_800_y_2}\n")
        print("Nombre empleado\t\tSueldo")
        for x in t_entre_800_y_2:
            print(f"{trabajadores[x]}\t\t${sueldos[x]}")
        print("\nSueldos superiores a $2.000.000")
        print(f"TOTAL: {mayor_2}\n")
        print("Nombre empleado\t\tSueldo")
        for x in t_mayor_2:
            print(f"{trabajadores[x]}\t\t${sueldos[x]}")
        total=0
        for x in sueldos:
            total+=x
        print(f"\nTOTAL SUELDOS: $ {total}\n")
        t_menor_800.clear()
        t_entre_800_y_2.clear()
        t_mayor_2.clear()

def opc_3():
    if not sueldos:
        print("Error! Primero debe asignarle un sueldo a los trabajadores!")
    else:
        print("\tVER ESTADÍSTICAS\n")
        sueldo_alto=400000
        sueldo_bajo=2600000
        promedio=0
        media=1
        for x in sueldos:
            promedio+=x
            media*=x
            if sueldo_bajo>=x:
                sueldo_bajo=x
            if sueldo_alto<x:
                sueldo_alto=x
        print(f"Sueldo más alto: $ {sueldo_alto}")
        print(f"Sueldo más bajo: $ {sueldo_bajo}")
        print(f"Promedio de sueldos: $ {promedio/10}")
        print(f"Media geométrica: $ {media**(1/10)}\n")

def opc_4():
    if not sueldos:
        print("Error! Primero debe asignarle un sueldo a los trabajadores!")
    else:
        print("\tREPORTE DE SUELDOS\n")

def opc_5():
    pass