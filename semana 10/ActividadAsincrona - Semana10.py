print("************************************")
print("*Bienvenido a nuestra tienda online*")
print("************************************\n")

#Variables
total = 0
totalF = 0

area1 = "Aparatos electronicos"
area2 = "Electrodomésticos"
area3 = "Muebles"
area4 = "Ropa"
area5 = "Limpieza"

print("En nuestra tienda online podra encontrar diversos productos electronicos:")

x = 1
while x:
    ElegirA = input(f"""\n\tÁreas disponibles
    1. {area1}
    2. {area2}
    3. {area3}
    4. {area4}
    5. {area5}
    
Elija un área -> """).lower()
    while x:
        #Area 1
        if ElegirA == area1.lower() or ElegirA == "1":
            prod1,prec1 = "Telefonos",116
            prod2,prec2 = "Tablets",245
            prod3,prec3 = "Laptops",435
            prod4,prec4 = "Play Station 5",540
            prod5,prec5 = "Nintendo Switch",345
            prod6,prec6 = "Televisores",1045

            print(f"\n\tÁrea de {area1}")
            print(f"""\tElija un producto:\n
        Productos               Precio
        1- {prod1}            ${prec1}
        2- {prod2}              ${prec2}
        3- {prod3}              ${prec3}
        4- {prod4}       ${prec4}
        5- {prod5}      ${prec5}
        6- {prod6}          ${prec6}\n""")

            orden = input("¿Qué desea comprar? -> ").lower()
            cantidad = int(input("Ingrese la cantidad -> "))

            if orden == prod1.lower() or orden == f"{prod1}s".lower() or orden == "1":
                total += prec1*cantidad

            elif orden == prod2.lower() or orden == f"{prod2}s".lower() or orden == "2":
                total += prec2*cantidad

            elif orden == prod3.lower() or orden == f"{prod3}s".lower() or orden == "3":
                total += prec3*cantidad

            elif orden == prod4.lower() or orden == "4":
                total += prec4*cantidad

            elif orden == prod5.lower() or orden == "5":
                total += prec5*cantidad

            elif orden == prod6.lower() or orden == f"{prod6}es".lower() or orden == "6":
                total += prec6*cantidad

            else:
                print("Esa opción no es válida")

            print(f"\nEl total a pagar: ${total}")

        #Area 2
        elif ElegirA == area2.lower() or ElegirA == "Electrodomesticos".lower() or ElegirA == "2":
            prod1,prec1 = "Refrigerador",289
            prod2,prec2 = "Licuadora",21
            prod3,prec3 = "Batidora",18
            prod4,prec4 = "Horno Microodas",85
            prod5,prec5 = "Lavadora",299
            prod6,prec6 = "Cocina electrica",15

            print(f"\n\tÁrea de {area2}")
            print(f"""\tElija un producto:\n
        Productos               Precio
        1- {prod1}         ${prec1}
        2- {prod2}            ${prec2}
        3- {prod3}             ${prec3}
        4- {prod4}      ${prec4}
        5- {prod5}             ${prec5}
        6- {prod6}     ${prec6}\n""")

            orden = input("¿Qué desea comprar? -> ").lower()
            cantidad = int(input("Ingrese la cantidad -> "))

            if orden == prod1.lower() or orden == f"{prod1}es".lower() or orden == "1":
                total += prec1*cantidad

            elif orden == prod2.lower() or orden == f"{prod2}s".lower() or orden == "2":
                total += prec2*cantidad

            elif orden == prod3.lower() or orden == f"{prod3}s".lower() or orden == "3":
                total += prec3*cantidad

            elif orden == prod4.lower() or orden == "4":
                total += prec4*cantidad

            elif orden == prod5.lower() or orden == f"{prod5}s".lower() or orden == "5":
                total += prec5*cantidad

            elif orden == prod6.lower() or orden == "6":
                total += prec6*cantidad

            else:
                print("Esa opción no es válida")

            print(f"\nEl total a pagar: ${total}")

        #Area 3
        elif ElegirA == area3.lower() or ElegirA == "3":
            prod1,prec1 = "Sillón familiar",459
            prod2,prec2 = "Sillón",216
            prod3,prec3 = "Mesa",59
            prod4,prec4 = "Silla",16
            prod5,prec5 = "Cama",123
            prod6,prec6 = "Estante",26

            print(f"\n\tÁrea de {area3}")
            print(f"""\tElija un producto:\n
        Productos              Precio
        1- {prod1}     ${prec1}
        2- {prod2}              ${prec2}
        3- {prod3}                ${prec3}
        4- {prod4}               ${prec4}
        5- {prod5}                ${prec5}
        6- {prod6}             ${prec6}\n""")

            orden = input("¿Qué desea comprar? -> ").lower()
            cantidad = int(input("Ingrese la cantidad -> "))

            if orden == prod1.lower() or orden == "1":
                total += prec1*cantidad

            elif orden == prod2.lower() or orden == f"{prod2}es".lower() or orden == f"sillon".lower() or orden == f"sillones".lower() or orden == "2":
                total += prec2*cantidad

            elif orden == prod3.lower() or orden == f"{prod3}s".lower() or orden == "3":
                total += prec3*cantidad

            elif orden == prod4.lower() or orden == f"{prod4}s".lower() or orden == "4":
                total += prec4*cantidad

            elif orden == prod5.lower() or orden == f"{prod5}s".lower() or orden == "5":
                total += prec5*cantidad

            elif orden == prod6.lower() or orden == f"{prod6}s".lower() or orden == "6":
                total += prec6*cantidad

            else:
                print("Esa opción no es válida")

            print(f"\nEl total a pagar: ${total}")

        #Area 4
        elif ElegirA == area4.lower() or ElegirA == "4":
            prod1,prec1 = "Camisa",7
            prod2,prec2 = "Pantalón",12
            prod3,prec3 = "Falda",15
            prod4,prec4 = "Calcetines",2
            prod5,prec5 = "Zapatos",36
            prod6,prec6 = "Gorra",10

            print(f"\n\tÁrea de {area4}")
            print(f"""\tElija un producto:\n
        Productos               Precio
        1- {prod1}               ${prec1}
        2- {prod2}             ${prec2}
        3- {prod3}                ${prec3}
        4- {prod4}           ${prec4}
        5- {prod5}              ${prec5}
        6- {prod6}                ${prec6}\n""")

            orden = input("¿Qué desea comprar? -> ").lower()
            cantidad = int(input("Ingrese la cantidad -> "))

            if orden == prod1.lower() or orden == f"{prod1}s".lower() or orden == "1":
                total += prec1*cantidad

            elif orden == prod2.lower() or orden == f"{prod2}es".lower() or orden == "2":
                total += prec2*cantidad

            elif orden == prod3.lower() or orden == f"{prod3}s".lower() or orden == "3":
                total += prec3*cantidad

            elif orden == prod4.lower() or orden == "calcetin".lower() or orden == "4":
                total += prec4*cantidad

            elif orden == prod5.lower() or orden == "zapato".lower() or orden == "5":
                total += prec5*cantidad

            elif orden == prod6.lower() or orden == f"{prod6}s".lower() or orden == "6":
                total += prec6*cantidad

            else:
                print("Esa opción no es válida")

            print(f"\nEl total a pagar: ${total}")

        #Area 5
        elif ElegirA == area5 or ElegirA == "5":
            prod1,prec1 = "Escoba",5
            prod2,prec2 = "Trapeador",5
            prod3,prec3 = "Jabón",2
            prod4,prec4 = "Esponja",2
            prod5,prec5 = "Trapos",3
            prod6,prec6 = "Guantes",7

            print(f"\n\tÁrea de {area5}")
            print(f"""\tElija un producto:\n
        Productos               Precio
        1- {prod1}               ${prec1}
        2- {prod2}            ${prec2}
        3- {prod3}                ${prec3}
        4- {prod4}              ${prec4}
        5- {prod5}               ${prec5}
        6- {prod6}              ${prec6}\n""")

            orden = input("¿Qué desea comprar? -> ").lower()
            cantidad = int(input("Ingrese la cantidad -> "))

            if orden == prod1.lower() or orden == f"{prod1}s".lower() or orden == "1":
                total += prec1*cantidad

            elif orden == prod2.lower() or orden == f"{prod2}es".lower() or orden == "2":
                total += prec2*cantidad

            elif orden == prod3.lower() or orden == f"{prod3}es".lower() or orden == "jabon".lower() or orden == "jabones".lower() or orden == "3":
                total += prec3*cantidad

            elif orden == prod4.lower() or orden == f"{prod4}s".lower() or orden == "4":
                total += prec4*cantidad

            elif orden == prod5.lower() or orden == "trapo".lower() or orden == "5":
                total += prec5*cantidad

            elif orden == prod6.lower() or orden == "guante".lower() or orden == "6":
                total += prec6*cantidad

            else:
                print("Esa opción no es válida")

            print(f"\nEl total a pagar: ${total}")

        else:
            print("Esa opción no es válida")
        
        NewOrden = input("\n¿Desea comprar algo mas? -> ").lower()
        break

    if NewOrden == "si".lower():
        print()
    
    else:
        break


#Descuento
if total >= 500 and total < 1000:
    totalF = total - (total * (5 / 100))
    saldo = int(input(f"\nUsted obtiene un descuento del 5% \nSu total a pagar con descuento es de: ${totalF} \nPor favor ingrese su paga -> "))

elif total > 1000:
    totalF = total - (total * (10 / 100))
    saldo = int(input(f"\nUsted obtiene un descuento del 10% \nSu total a pagar con descuento es de: ${totalF} \nPor favor ingrese su paga -> "))

elif total < 500:
    totalF = total
    saldo = int(input(f"""\nSu total a pagar es: ${totalF} \nPor favor ingrese su paga -> """))

#Cobrar al cliente
"""saldo = int(input(f\nSu total a pagar es: {totalF}\nPor favor ingrese su paga -> ))"""

#Cambio
if saldo >= totalF:
    if saldo > totalF:
        print(f"\nSu cambio es de: ${saldo - totalF}\n'Gracias por su compra'")

    elif saldo == totalF:
        print("\n'Gracias por su compra'")

elif saldo < totalF:
    print("\nUsted no cuenta con dinero suficiente")


print("\nFin del programa")