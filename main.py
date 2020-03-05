opcion = 1
Cuentas = {}
Cargo = {}
Credito = {}
Acumulado = []
print(type(Credito))
while opcion >= 0:
    opcion = (int(input((("_"*160) + "\n\nHola, ¿Que accion quieres realizar?: \n\n* Registrar una cuenta = ( 1 ) \n\n* Registrar un nuevo movimiento = ( 2 ) \n\n* Obtener el saldo de una cuenta = ( 3 )\n\n* Salir = ( 4 ) \n:"))))
    if opcion <0 and opcion > 5:
        opcion = (int(input((("_"*80) + "\n\nHola, ¿Que accion quieres realizar?: \n\n* Registrar una cuenta = ( 1 ) \n\n* Registrar un nuevo movimiento = ( 2 ) \n\n* Obtener el saldo de una cuenta = ( 3 )\n\n* Salir = ( 4 ) \n:"))))
    while opcion > 0 and opcion < 5:                          
        while opcion == 1:
            Codigo = int(input("Dame el codigo de la cuenta: "))
            NombreCuenta = input("Dame el nombre de la cuenta: ")
            Cuentas [Codigo] = NombreCuenta
            Cargo [Codigo] = []
            Credito [Codigo] = []
            opcion = int(input("\nQuieres añadir otra cuenta? ( 1 ) \nSalir ( 2 ) \n :"))
            if opcion == 1:
                opcion = 1
            else:
                opcion = 0
                print(f"Estas son las cuentas existentes: {Cuentas}")

        respuesta = 1
        while opcion == 2:
            if  respuesta == 1:
                Codigo = int(input(("_"*100)+"\n\nDame el codigo de de la cuenta: "))
                MovimientoTipo = int(input(f"¿Que tipo de movimiento quieres realizar con la cuenta {Cuentas[Codigo]}? \n\n Cargo ( 1 ) Credito ( 2 ) \n\n SALIR ( 3 )\n\n: "))

            while MovimientoTipo == 1:
                
                Confirmacion = int(input(f"Estas seguro que quieres afectar con un CARGO la cuenta {Cuentas[Codigo]}? \n\n    SI ( 1 )  \n\n    NO ( 2 ) \n\n"))
                if Confirmacion == 2:
                    MovimientoTipo = 0
                    opcion = 0
                while Confirmacion == 1:  
                    Monto = float(input("Dame el monto: "))
                    ((Cargo[Codigo]).append(Monto))
                    respuesta = int(input(f"\nQuieres añadir otro CARGO a la cuenta? \n\nSi ( 1 ) \nSalir ( 2 ) \n : "))
                    if respuesta != 1:
                        Confirmacion = 0
                        MovimientoTipo = 0
                        opcion = 0
                        print(f"La cuenta {Cuentas[Codigo]} cuenta con los siguientes cargos: {Cargo[Codigo]} \n\nY el total de los cargos suma la cantidad de {sum(Cargo[Codigo])}")
                  
            while MovimientoTipo == 2:
                Codigo = int(input(("_"*100)+"\n\nDame el codigo de de la cuenta: "))
                Confirmacion = int(input(f"Estas seguro que quieres afectar con un CREDITO la cuenta {Cuentas[Codigo]}? \n\n    SI ( 1 )  \n\n    NO ( 2 ) \n\n"))
                if Confirmacion == 2:
                    MovimientoTipo = 0
                    opcion = 0
                while Confirmacion == 1:
                    Monto = float(input("Dame el monto: "))
                    ((Credito[Codigo]).append(Monto))
                    respuesta = int(input(f"\nQuieres añadir otro CREDITO a la cuenta? \n\nSi ( 1 ) \nSalir ( 2 ) \n : "))
                    if respuesta != 1:
                        Confirmacion = 0
                        MovimientoTipo = 0
                        opcion = 0
                        print(f"La cuenta {Cuentas[Codigo]} cuenta con los siguientes creditos: {Cargo[Codigo]} \n\nY el total de los creditos suma la cantidad de {sum(Credito[Codigo])}")
            if MovimientoTipo == 3:
                opcion = 0
                    
        while opcion == 3:
            Consulta = int(input("\n\n\n¿Cual es el codigo de la cuenta que desas consultar? \n : "))
            Saldo = (sum(Cargo[Consulta])) - (sum(Credito[Consulta]))
                
            if Saldo > 0:
                print(f"El saldo de la cuenta {Cuentas[Consulta]} es de naturaleza = ACREEDORA \n Y su saldo es de: {Saldo} $.")
            else:
                print(f"El saldo de la cuenta {Cuentas[Consulta]} es de naturaleza = DEUDORA \n Y su saldo es de: {Saldo} $.")
            opcion = 0
        if opcion == 4:
            opcion = -1       
