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
    pass

def opc_4():
    pass

def opc_5():
    pass