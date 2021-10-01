from random import uniform
from random import randint

#Esta función da a elegir al usuario el banner del cual obtener información.

def info_banner():
    banner = input("De que banner quieres saber información?\nBanner permanente (opcion 1)\nBanner de armas (opcion 2)\n"   
                   "Banner de promocion (opcion 3)\n")
    if banner == "1":
        print("Este banner es un deseo estándar sin límite de tiempo. Hay disponibles armas y personajes\nno "
              "promocionales. En este deseo, garantiza ganar un artículo de 4 estrellas o superior al\nmenos una vez "
              "cada 10 intentos.")
        print("Probabilidad personaje de 5 estrellas = 0.300% y probabilidad arma de 5 estrellas = 0.300%,\ntienes "
              "garantizado ganar un artículo de 5 estrellas al menos una vez cada 90 intentos.")
        print("Probabilidad personaje de 4 estrellas = 2.550% y probabilidad arma de 4 estrellas = 2.550%,\ntienes "
              "garantizado ganar un artículo de 4 estrellas o superior al menos una vez cada 10 intentos\n")

    elif banner == "2":
        print("Probabilidad arma de 5 estrellas = 0,700%; tienes garantizado ganar un arma de 5 estrellas\nal menos una "
              "vez cada 80 intentos. Primer arma de 5 estrellas en este evento\n= 75% de probabilidad de que sea una de "
              "las armas promocionales. Si primer arma\nde 5 estrellas no es una de las armas promocionales, entonces "
              "próxima arma de 5\nestrellas = 100% arma promocional.")
        print("Probabilidad personaje de 4 estrellas = 3.000% y probabilidad arma de 4 estrellas = 3.000%;\ngarantizado "
              "para ganar un artículo de 4 estrellas o superior al menos una vez cada 10 intentos.")
        print("La primera vez que ganes un artículo de 4 estrellas = 75% de probabilidad de\nque sea una de las armas "
              "destacadas. Si el primer artículo de 4 estrellas que\nganas no es una de las armas destacadas, el "
              "siguiente artículo de 4 estrellas = 100%\nde probabilidad de ser un arma destacada.\n")

    elif banner == "3":
        print("Probabilidad personaje de 5 estrellas = 0,600%; tienes garantizado ganar un personaje de 5 estrellas\nal "
              "menos una vez cada 90 intentos. Primer artículo de 5 estrellas = 50% de\nprobabilidad de que sea el "
              "personaje promocional. Si primer personaje de 5 estrellas no es\nun personaje promocional, entonces el "
              "siguiente personaje de 5 estrellas = 100% personaje promocional.")
        print("Probabilidad artículo de 4 estrellas = 5.100%; garantizado para ganar un artículo de 4 estrellas\no "
              "superior al menos una vez cada 10 intentos. Primer artículo de 4 estrellas = 50%\nde probabilidad de que "
              "sea un personaje promocional. Si el primer elemento de 4 estrellas\nno es uno de los personajes "
              "destacados, entonces siguiente elemento de 4 estrellas = 100% personaje promocional.\n")

    else:
        print("Disculpa, esa no es ninguna de las opciones")
        info_banner()

#Esta función ayuda al usuario a calcular la cantidad de destinos que puede obtener a traves del uso de diversas monedas
#del juego, además de calcular el reembolso minimo de esta transaccion.

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

#Esta función calcula en base de los destinos del usuario, si este podra activar el sistema que grantiza un personaje
#de 5 estrellas.

def pity():
    deseos = int(input("Cuantos destinos tienes?\n"))
    predeseos = int(input("Cuantos deseos has pedido desde la ultima vez que tuviste un personaje de 5 estrellas?\n"))
    deseostot = deseos + predeseos
    pity = 90 - deseostot
    if deseostot < 90:
        print("Te faltarian",pity,"para un personaje de 5 estrellas garantizado")
    elif deseostot >= 90:
        print("Tienes suficientes deseos para activar el sistema de pity")

#Esta función hace una simulación del sistema de gacha del juego de un deseo a la vez, puede ayudar a los jugadores
#adictos a esta mecanica sin que necesiten gastar su moneda del juego.

def gacha():
    banner = input("En que banner quieres desear?\nBanner permanente (opcion 1)\nBanner de armas (opcion 2)\n"   
                    "Banner de promocion (opcion 3)\n")
    if banner == "1":
        chara5 = ["Jean","Diluc","Mona","Keching","Qiqi" ]
        chara5num = randint(0,4)
        weap5 = ["Arco de amos","Alas celestiales","Oración Perdida a los Vientos Sagrados","Pergamino Celestial"]
        weap5num = randint(0,3)
        chara4 = ["Diona","Razor","Beidou","Bennet"]
        chara4num = randint(0,3)
        weap4 = ["Herrumbre","Arco del sacrificio","Ultimo acorde","Ojo de la perspicacia"]
        weap4num = randint(0,3)
        prob = uniform(0,100)
        if prob <= 0.3:
            print("Obtuviste a", chara5[chara5num])
        elif (prob <= 0.6) and (prob > 0.3):
            print("Obtuviste", weap5[weap5num])
        elif (prob <= 3.15) and (prob > 0.6):
            print("Obtuviste a", chara4[chara4num])
        elif (prob <= 5.7) and (prob > 3.15):
            print("Obtuviste", weap4[weap4num])
        else:
            print("Obtuviste un arma de 3 estrellas :(")

    elif banner == "2":
        weap5 = ["Luna inalterable","Cortador de Jade primordial","Halcón de jade","Lápida del lobo"]
        weap5num = randint(0, 3)
        chara4 = ["Diona", "Razor", "Beidou", "Bennet"]
        chara4num = randint(0, 3)
        weap4 = ["Códice de Favonius","Segadora de la lluvia","Perdición del dragon","Gran espada de sacrificio"]
        weap4num = randint(0, 3)
        prob = uniform(0, 100)
        if prob <= 0.7:
            print("Obtuviste", weap5[weap5num])
        elif (prob <= 3.7) and (prob > 0.7):
            print("Obtuviste", weap4[weap4num])
        elif (prob <= 6.7) and (prob > 3.7):
            print("Obtuviste a", chara4[chara4num])
        else:
            print("Obtuviste un arma de 3 estrellas :(")

    elif banner == "3":
        chara5 = ["Sangonomiya","Jean","Diluc","Mona","Keching","Qiqi"]
        chara5num = randint(0, 5)
        chara4 = ["Diona", "Xingchiu", "Beidou", "Rosaria"]
        chara4num = randint(0, 3)
        weap4 = ["Flauta","Rugido del leon","Espada del tiempo","Memorias de sacrificios"]
        weap4num = randint(0, 3)
        prob = uniform(0,100)
        if prob <= 0.6:
            print("Obtuviste a", chara5[chara5num])
        elif (prob <= 3.15) and (prob > 0.6):
            print("Obtuviste", weap4[weap4num])
        elif (prob <= 5.7) and (prob > 3.15):
            print("Obtuviste a", chara4[chara4num])
        else:
            print("Obtuviste un arma de 3 estrellas :(")

#Frase mencionada al inicio del programa para proveer contexto al usuario.

print("En genshin impact hay un sistema de gacha el cual tiene un sistema de pity,\nel cual te garantiza un personaje "
      "de 5 estrellas, para garantizar ese personaje es necesario\npedir 90 deseos desde la ultima vez que tuviste un "
      "personaje de 5 estrellas")

#Loop while usado para repetir el menu inicial siempre y cuando el usuario lo quiera a traves de la veriable "reinicio"
#la cual si se mantiene con un valor de "si" repetira el menu. En cualquier otro caso se le dara las gracias al usuario
#y el programa se detendra.

reinicio = "si"
reiniciogacha = "si"

while reinicio == "si":
    funcion = input("Que quieres hacer?\nChecar tus probabilidades (opcion 1)\nCalcular tus deseos faltantes para un "
                    "personaje de 5 estrellas (opcion 2)\nCalcular cuantos destinos puedes obtener (opcion 3)\n"
                    "Simulación de gacha <NEW> (opcion 4)\n")
    if funcion == "1":
        info_banner()
        reinicio = input("Volver al menu?\n")
    elif funcion == "2":
        pity()
        reinicio = input("Volver al menu?\n")
    elif funcion == "3":
        destinos()
        reinicio = input("Volver al menu?\n")
    elif funcion == "4":
        while reiniciogacha == "si":
            gacha()
            reiniciogacha = input("Deseas probar tu suerte de nuevo?\n")
        reinicio = input("Volver al menu?\n")
    else:
        print("No hay esa opcion")
        reinicio = input("Volver al menu?\n")
print("Gracias por usar este programa")