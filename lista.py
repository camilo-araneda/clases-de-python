cargos=["ceo","analista","programadores"]

def seleccionar_cargo():
    while True:
        for i in range(len(cargos)):
            print(f"{i+1} {cargos[i]}")
        opcion_cargo=int(input("Ingrese un cargo"))
        
        if opcion_cargo < 1 and opcion_cargo > len(cargos):
            print("opcion ingresada no valida")
        else:
            cargo=cargos[opcion_cargo-1]
    return cargo
            
        
def crearUsuario():
    nombre = input("ingrese su nombre")
    cargo = seleccionar_cargo()
    sueldo = int(input("ingrese su sueldo"))
#Calcular_descuento
    descuento_salud=sueldo*0.07
    descuento_afp=sueldo*0.12
    liquido_pagar=

    
while True:
    print("----------------------------------------------")
    print ("1.-Registrar trabajadores")
    print ("2.-Listar a todos los trabajadores")
    print ("3.-Imprimir planilla de sueldos")
    print ("4.-Salir del Programa")
    print("----------------------------------------------")

opcionIngresada = int(input("ingrese una opcion"))

match opcionIngresada:
    case 1:
    case 2:
    case 3:
    case 4:
        