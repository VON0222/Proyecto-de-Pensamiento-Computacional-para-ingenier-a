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
        print("Este banner es un deseo estándar sin límite de tiempo. Hay disponibles armas y personajes\nno promocionales. En este deseo, "
              "garantiza ganar un artículo de 4 estrellas o superior al\nmenos una vez cada 10 intentos.")
        print("Probabilidad personaje de 5 estrellas = 0.300% y probabilidad arma de 5 estrellas = 0.300%,\ntienes garantizado ganar un"
              " artículo de 5 estrellas al menos una vez cada 90 intentos.")
        print("Probabilidad personaje de 4 estrellas = 2.550% y probabilidad arma de 4 estrellas = 2.550%,\ntienes garantizado ganar un"
              " artículo de 4 estrellas o superior al menos una vez cada 10 intentos\n")
        regresar()

    elif banner == "2":
        print("Probabilidad arma de 5 estrellas = 0,700%; tienes garantizado ganar un arma de 5 estrellas\nal menos una vez cada 80 intentos."
              " Primer arma de 5 estrellas en este evento\n= 75% de probabilidad de que sea una de las armas promocionales. Si primer arma\n"
              "de 5 estrellas no es una de las armas promocionales, entonces próxima arma de 5\nestrellas = 100% arma promocional.")
        print("Probabilidad personaje de 4 estrellas = 3.000% y probabilidad arma de 4 estrellas = 3.000%;\ngarantizado para ganar"
              " un artículo de 4 estrellas o superior al menos una vez cada 10 intentos.")
        print("La primera vez que ganes un artículo de 4 estrellas = 75% de probabilidad de\nque sea una de las armas destacadas. Si el primer"
              " artículo de 4 estrellas que\nganas no es una de las armas destacadas, el siguiente artículo de 4 estrellas = 100%\nde probabilidad"
              " de ser un arma destacada.\n")
        regresar()

    elif banner == "3":
        print("Probabilidad personaje de 5 estrellas = 0,600%; tienes garantizado ganar un personaje de 5 estrellas\nal menos una vez cada"
              " 90 intentos. Primer artículo de 5 estrellas = 50% de\nprobabilidad de que sea el personaje promocional. Si primer personaje de"
              " 5 estrellas no es\nun personaje promocional, entonces el siguiente personaje de 5 estrellas = 100% personaje promocional.")
        print("Probabilidad artículo de 4 estrellas = 5.100%; garantizado para ganar un artículo de 4 estrellas\no superior al menos una vez"
              " cada 10 intentos. Primer artículo de 4 estrellas = 50%\nde probabilidad de que sea un personaje promocional. Si el primer elemento"
              " de 4 estrellas\nno es uno de los personajes destacados, entonces siguiente elemento de 4 estrellas = 100% personaje promocional.\n")
        regresar()

    else:
        print("Disculpa, esa no es ninguna de las opciones")
        info_banner()

def destinos():
    primos = int(input("Cuantas primogemas tienes?\n"))
    polvo = int(input("Cuanto polvo estelar tienes?\n"))
    brillo = int(input("Cuanto brillo estelar tienes?\n"))
    deseos_prim = int(primos/160)
    deseos_polv = int(polvo/75)
    deseos_brill = int(brillo/160)
    deseos = deseos_prim + deseos_polv + deseos_brill
    reembolso = deseos*5
    deseosreem = int(reembolso/75)
    print("Puedes pedir",deseos,"deseos")
    print("Te reembolsaria minimo", reembolso, "de polvo estelar")
    print("Y con el rembolso podrias comprar", deseosreem, "deseo(s)")
    regresar()

def pity():
    deseos = int(input("Cuantos destinos tienes?"))
    predeseos = int(input("Cuantos deseos has pedido desde la ultima vez que tuviste un personaje de 5 estrellas?\n"))
    deseostot = deseos + predeseos
    pity = 90 - deseostot
    if deseostot < 90:
        print("Te faltarian",pity,"para un personaje de 5 estrellas garantizado")
    elif deseostot >= 90:
        print("Tienes suficientes deseos para activar el sistema de pity")
    regresar()

print("En genshin impact hay un sistema de gacha el cual tiene un sistema de pity,\nel cual te garantiza un personaje de 5 estrellas, "
      "para garantizar ese personaje es necesario\npedir 90 deseos desde la ultima vez que tuviste un personaje de 5 estrellas")

menu()
