print("En genshin impact hay un sistema de gacha el cual tiene un sistema de pity,\nel cual te garantiza un personaje de 5 estrellas "
      "para garantizar ese personaje\n es necesario pedir 90 deseos desde la ultima vez que tuviste un personaje de 5 estrellas\n"
      " y cada deseo cuesta 160 primogemas")
primos = int(input("Cuantas primogemas tienes?\n"))
predeseos = int(input("Cuantos deseos has pedido desde la ultima vez que tuviste un personaje de 5 estrellas?\n"))
deseos = int(primos/160)
pity = 90-predeseos-deseos
print("Puedes pedir",deseos,"deseos")

if deseos<90:
    print("Te faltarian",pity,"para un personaje de 5 estrellas garantizado")
elif deseos>90:
    print("Tienes suficientes deseos para activar el sistema de pity")