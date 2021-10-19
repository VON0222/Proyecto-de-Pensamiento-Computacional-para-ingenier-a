"""
Este programa esta diseñado para ayudar a jugadores de Genshin Impact a
través de funciones que dan información sobre los banner del sistema de
gacha del juego, calculan la cantidad de una divisa del juego que el
usuario posee, calculan si a traves de las divisas que poseen el usuario
puede activar el sistema de pity programado en el juego y generan
simulaciones similares al sistema de gacha del juego.
Este programa fue programado por José Diego Llaca Castro,
matricula A01704793, como proyecto para la materia de Pensamiento
Computacional para Ingeniería

En este codigo se uso la libreria random de la pagina
https://docs.python.org/3/library/random.html la cual contiene la
función "uniform" la cual genera un numero decimal aletorio entre dos
valores dados a la función y "randint" la cual genera un numero entero
aleatorio entre dos valores dados a la función.
En este codigo use esas dos funciones para hacer una funcion la cual
saca elementos de listas de acuerdo a los numeros aleatorios para
simular un sistema de probabilidad.
"""

from random import uniform
from random import randint


def info_banner(bannerinf):

    """
    Función: Muestra la información de cada banner del juego y las
    probabilidades de obtención en base a la elección del usuario.
    Parametros: Bannerinf, valor numerico entero.
    Devuelve: Imprime texto.
    """

    if bannerinf == "1":

        print("Este banner es un deseo estándar sin límite de tiempo. Hay disponibles "
              "armas y personajes\nno promocionales. En este deseo, garantiza ganar un "
              "artículo de 4 estrellas o superior al\nmenos una vez cada 10 intentos.")

        print("Probabilidad personaje de 5 estrellas = 0.300% y probabilidad arma de 5 "
              "estrellas = 0.300%,\ntienes garantizado ganar un artículo de 5 estrellas al "
              "menos una vez cada 90 intentos.")

        print("Probabilidad personaje de 4 estrellas = 2.550% y probabilidad arma de 4 "
              "estrellas = 2.550%,\ntienes garantizado ganar un artículo de 4 estrellas o "
              "superior al menos una vez cada 10 intentos\n")

    elif bannerinf == "2":

        print("Probabilidad arma de 5 estrellas = 0,700%; tienes garantizado ganar un "
              "arma de 5 estrellas\nal menos una vez cada 80 intentos. Primer arma de 5 "
              "estrellas en este evento\n= 75% de probabilidad de que sea una de las armas "
              "promocionales. Si primer arma\nde 5 estrellas no es una de las armas "
              "promocionales, entonces próxima arma de 5\nestrellas = 100% arma promocional.")

        print("Probabilidad personaje de 4 estrellas = 3.000% y probabilidad arma de 4 "
              "estrellas = 3.000%;\ngarantizado para ganar un artículo de 4 estrellas o "
              "superior al menos una vez cada 10 intentos.")

        print("La primera vez que ganes un artículo de 4 estrellas = 75% de "
              "probabilidad de\nque sea una de las armas destacadas. Si el primer artículo de"
              " 4 estrellas que\nganas no es una de las armas destacadas, el siguiente "
              "artículo de 4 estrellas = 100%\nde probabilidad de ser un arma destacada.\n")

    elif bannerinf == "3":

        print("Probabilidad personaje de 5 estrellas = 0,600%; tienes garantizado ganar"
              " un personaje de 5 estrellas\nal menos una vez cada 90 intentos. Primer "
              "artículo de 5 estrellas = 50% de\nprobabilidad de que sea el personaje "
              "promocional. Si primer personaje de 5 estrellas no es\nun personaje "
              "promocional, entonces el siguiente personaje de 5 estrellas = 100% personaje "
              "promocional.")

        print("Probabilidad artículo de 4 estrellas = 5.100%; garantizado para ganar un"
              " artículo de 4 estrellas\no superior al menos una vez cada 10 intentos. Primer"
              " artículo de 4 estrellas = 50%\nde probabilidad de que sea un personaje "
              "promocional. Si el primer elemento de 4 estrellas\nno es uno de los personajes"
              " destacados, entonces siguiente elemento de 4 estrellas = 100% personaje "
              "promocional.\n")

    else:

        print("Disculpa, esa no es ninguna de las opciones")
        bannerinf = input("De que banner quieres saber información?\nBanner permanente "
                          "(opcion 1)\nBanner de armas (opcion 2)\nBanner de promocion (opcion 3)\n")
        info_banner(bannerinf)


def destinos(primos, polvo, brillo):

    """
    Función: Operaciónes matematicas para obtener la transformación de los
    parametros recibidos en otras variables las cuales se devolveran al
    usuario.
    Parametros: Primos, valor numerico entero, Polvo, valor numerico entero,
    brillo, valor numerico entero.
    Devuelve: Imprime texto en donde contiene calculos de las variables
    deseos_calc, reembolso y deseosreem.
    """

    deseos_prim = int(primos/160)
    deseos_polv = int(polvo/75)
    deseos_brill = int(brillo/160)
    deseos_calc = deseos_prim + deseos_polv + deseos_brill
    reembolso = deseos_calc * 5
    deseosreem = int(reembolso/75)

    print("Puedes pedir", deseos_calc, "deseos")
    print("Te reembolsaria minimo", reembolso, "de polvo estelar")
    print("Y con el rembolso podrias comprar", deseosreem, "deseo(s)")


def pity(deseos, predeseos):

    """
    Función: Operaciones matematicas para obtener una variable y dependiendo
    del valor de esta variable se imprime un texto u otro.
    Parametros: deseos, valor numerico entero, predeseos, valor numerico entero.
    Devuelve: Imprime un texto en caso de cumplir una condición, si no se
    cumple, imprime texto que contiene la variable pity_calc.
    """

    deseostot = deseos + predeseos
    pity_calc = 90 - deseostot

    if deseostot < 90:
        print("Te faltarian", pity_calc, "deseos para un personaje de 5 estrellas "
                                         "garantizado")

    elif deseostot >= 90:
        print("Tienes suficientes deseos para activar el sistema de pity")


def gacha(banner_gacha):

    """
    Función: Genera un numero aleatorio con la función randint() y uniform()
    y en base a ese numero se imprimen strings contenidos en listas y se
    guardan en otras listas.
    Parametro: banner_gacha, valor numerico entero.
    Devuelve: Imprime un string sacado de una lista.
    """

    if banner_gacha == "1":
        chara5 = ["Jean", "Diluc", "Mona", "Keching", "Qiqi"]
        chara5num = randint(0, 4)
        weap5 = ["Arco de amos", "Alas celestiales",
                 "Oración Perdida a los Vientos Sagrados", "Pergamino Celestial"]
        weap5num = randint(0, 3)
        chara4 = ["Diona", "Razor", "Beidou", "Bennet"]
        chara4num = randint(0, 3)
        weap4 = ["Herrumbre", "Arco del sacrificio", "Ultimo acorde",
                 "Ojo de la perspicacia"]
        weap4num = randint(0, 3)

        if len(sesionp) == 89:
            prob = 0.2
        else:
            prob = uniform(0, 100)

        if prob <= 0.3:
            print("Obtuviste a", chara5[chara5num])
            sesionp.append(chara5[chara5num])
        elif (prob <= 0.6) and (prob > 0.3):
            print("Obtuviste", weap5[weap5num])
            sesionp.append(weap5[weap5num])
        elif (prob <= 3.15) and (prob > 0.6):
            print("Obtuviste a", chara4[chara4num])
            sesionp.append(chara4[chara4num])
        elif (prob <= 5.7) and (prob > 3.15):
            print("Obtuviste", weap4[weap4num])
            sesionp.append(weap4[weap4num])
        else:
            print("Obtuviste un arma de 3 estrellas :(")
            sesionp.append("debate club")

    elif banner_gacha == "2":
        weap5 = ["Luna inalterable", "Cortador de Jade primordial", "Halcón de jade",
                 "Lápida del lobo"]
        weap5num = randint(0, 3)
        chara4 = ["Diona", "Razor", "Beidou", "Bennet"]
        chara4num = randint(0, 3)
        weap4 = ["Códice de Favonius", "Segadora de la lluvia", "Perdición del dragon",
                 "Gran espada de sacrificio"]
        weap4num = randint(0, 3)

        if len(sesiona) == 79:
            prob = 0.5
        else:
            prob = uniform(0, 100)

        if prob <= 0.7:
            print("Obtuviste", weap5[weap5num])
            sesiona.append(weap5[weap5num])
        elif (prob <= 3.7) and (prob > 0.7):
            print("Obtuviste", weap4[weap4num])
            sesiona.append(weap4[weap4num])
        elif (prob <= 6.7) and (prob > 3.7):
            print("Obtuviste a", chara4[chara4num])
            sesiona.append(chara4[chara4num])
        else:
            print("Obtuviste un arma de 3 estrellas :(")
            sesiona.append("debate club")

    elif banner_gacha == "3":
        chara5 = ["Sangonomiya", "Jean", "Diluc", "Mona", "Keching", "Qiqi"]
        chara5num = randint(0, 5)
        chara4 = ["Diona", "Xingchiu", "Beidou", "Rosaria"]
        chara4num = randint(0, 3)
        weap4 = ["Flauta", "Rugido del leon", "Espada del tiempo",
                 "Memorias de sacrificios"]
        weap4num = randint(0, 3)

        if len(sesionpr) == 89:
            prob = 0.5
        else:
            prob = uniform(0, 100)

        if prob <= 0.6:
            print("Obtuviste a", chara5[chara5num])
            sesionpr.append(chara5[chara5num])
        elif (prob <= 3.15) and (prob > 0.6):
            print("Obtuviste", weap4[weap4num])
            sesionpr.append(weap4[weap4num])
        elif (prob <= 5.7) and (prob > 3.15):
            print("Obtuviste a", chara4[chara4num])
            sesionpr.append(chara4[chara4num])
        else:
            print("Obtuviste un arma de 3 estrellas :(")
            sesionpr.append("debate club")


"""
Definiciones iniciales para varibles y listas usadas en el codigo.
Las variables son reinicio, es un string, reiniciogacha, es un string,
historial, es una matriz, sesionp, es una lista, sesiona, es una lista y
sesionpr, es una lista.
"""


reinicio = "si"
reiniciogacha = "si"
historial = []
sesionp = []
sesiona = []
sesionpr = []

# Impresion de una frase mencionada al inicio del programa para proveer contexto al usuario.


print("En genshin impact hay un sistema de gacha el cual tiene un sistema de "
      "pity,\nel cual te garantiza un personaje de 5 estrellas, para garantizar ese "
      "personaje es necesario\npedir 90 deseos desde la ultima vez que tuviste un "
      "personaje de 5 estrellas")


"""
Función: Loop while usado para repetir el menu inicial siempre y cuando
el usuario lo quiera a traves de la variable "reinicio".
Dentro del while pide el valor de la variable función, la cual es un
valor numerico entero.
Dependiendo de el valor de la variable se pide input para ciertas
variables y se inician ciertas funciones.
"""


while reinicio == "si":
    funcion = input("Que quieres hacer?\nChecar tus probabilidades (opcion 1)\n"
                    "Calcular tus deseos faltantes para un personaje de 5 estrellas (opcion 2)\n"
                    "Calcular cuantos destinos puedes obtener (opcion 3)\nSimulación de gacha <NEW>"
                    " (opcion 4)\n")

    if funcion == "1":
        banner = input("De que banner quieres saber información?\nBanner permanente "
                       "(opcion 1)\nBanner de armas (opcion 2)\nBanner de promocion (opcion 3)\n")
        info_banner(banner)
        reinicio = input("Volver al menu?\n")

    elif funcion == "2":
        u_deseos = int(input("Cuantos destinos tienes?\n"))
        u_predeseos = int(input("Cuantos deseos has pedido desde la ultima vez que "
                                "tuviste un personaje de 5 estrellas?\n"))
        pity(u_deseos, u_predeseos)
        reinicio = input("Volver al menu?\n")

    elif funcion == "3":
        u_primos = int(input("Cuantas primogemas tienes?\n"))
        u_polvo = int(input("Cuanto polvo estelar tienes?\n"))
        u_brillo = int(input("Cuanto brillo estelar tienes?\n"))
        destinos(u_primos, u_polvo, u_brillo)
        reinicio = input("Volver al menu?\n")

    elif funcion == "4":
        while reiniciogacha == "si":
            banner = input("En que banner quieres desear?\nBanner permanente (opcion 1)\n"
                           "Banner de armas (opcion 2)\nBanner de promocion (opcion 3)\n")
            gacha(banner)
            reiniciogacha = input("Deseas probar tu suerte de nuevo?\n")

        historial.append(sesionp)
        historial.append(sesiona)
        historial.append(sesionpr)
        reiniciogacha = "si"

        print("Lo que obtuviste de esta sesion fue")
        for listas in historial:
            for elemhistorial in listas:
                print(elemhistorial)
        reinicio = input("Volver al menu?\n")

    else:
        print("No hay esa opcion")
        reinicio = input("Volver al menu?\n")

print("Gracias por usar este programa")
