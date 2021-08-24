print("En genshin impact hay un sistema de gacha el cual tiene un sistema de pity,\nel cual te garantiza un personaje de 5 estrellas, "
      "para garantizar ese personaje\nes necesario pedir 90 deseos desde la ultima vez que tuviste un personaje de 5 estrellas")

def menu():
    funcion = input("Que quieres hacer?\nChecar tus probabilidades opcion 1\nCalcular tus deseos faltantes para un personaje de 5 estrellas "
                "opcion 2\nCalcular cuantos destinos puedes obtener opcion 3\n")
    if funcion == "1":
        info_banner()
    elif funcion == "2":
        pity()
    elif funcion == "3":
        destinos()
    else:
        print("No hay esa opcion")

def regresar():
    reinicio = input("Desea regresar?\n")
    if reinicio == "si":
        menu()
    else:
        print("Gracias por usar este programa")

def info_banner():
    banner = input("De que banner quieres saber información?\nBanner permanente opcion 1\nBanner de armas opcion 2\nBanner de promocion 3\n")
    if banner == "1":
        print("Insertar info banner1")
        regresar()

    elif banner == "2":
        print("Insertar info banner2")
        regresar()

    elif banner == "3":
        print("Insertar info banner3\n")
        regresar()

    else:
        print("Disculpa esa no es ninguna de las opciones")
        info_banner()

def destinos():
    primos = int(input("Cuantas primogemas tienes?\n"))
    polvo = int(input("Cuanto polvo estelar tienes?\n"))
    brillo = int(input("Cuanto brillo estelar tienes?\n"))
    deseos_prim = int(primos/160)
    deseos_polv = int(polvo/75)
    deseos_brill = int(brillo/160)
    deseos = deseos_prim + deseos_polv + deseos_brill
    print("Puedes pedir",deseos,"deseos")
    regresar()

def pity():
    deseos = int(input("Cuantos destinos tienes?"))
    predeseos = int(input("Cuantos deseos has pedido desde la ultima vez que tuviste un personaje de 5 estrellas?\n"))
    deseostot = deseos + predeseos
    pity = 90 - deseostot
    if deseostot < 90:
        print("Te faltarian",pity,"para un personaje de 5 estrellas garantizado")
    elif deseostot > 90:
        print("Tienes suficientes deseos para activar el sistema de pity")
    regresar()

menu()
