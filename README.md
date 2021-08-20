# Proyecto-de-Pensamiento-Computacional-para-ingenieria

Debido a mi interes en los videojuegos y mi reciente obsesion con un sistema basado en probabilidades he decidido crear un codigo que ayude a los jugadores de Genshin Impact a saber que probabilidades tienen de obtener un personaje de 5 estrellas, tanto en el banner promocional como en el banner fijo, saber cuantos destinos (moneda del juego) serian necesarios para ello y mantener la cuenta de los destinos faltantes para activar el sistema de pity en cualquiera de los banners.

Conforme este proyecto evolucione, funciones mas complejas seran añadidas. El objetivo final es crear un programa que realmente ayude a los jugadores de este juego a llevar un buen registro y saber exactamente cuantos destinos deberan usar para obtener el personaje que desean. 

Considero que este proyecto es interesante ya que un amplio porcentaje de la comunidad de Genshin Impact suele llevar un registro de este sistema de gacha, sin embargo lo llevan de manera mental o directamente cada vez que accesan al juego revisan los registros para calcular en que punto se encuentran. Esto a pesar de ser efectivo es muy rudimentario y cansado a la larga (Hablando desde la experiencia) es por esto que este programa deberia ser un tanto útil para estos jugadores, sin embargo, tambien me parece que podria ser útil para los jugadores que no conocen bien el funcionamiento del sistema de este juego, ya que podria informarles del funcionamiento y ayudarlos a empezar a usarlo a su favor.

Algoritmo:

E0(funcion)
  si funcion = 1
    Pedir cantidad de destinos
    destinos faltantes = 90 - cantidad de destinos 
    pedir destinos posibles
    destinos para 5 estrellas = destinos faltantes - destinos posibles
    imprimir destinos para 5 estrellas
  si funcion = 2
    pedir numero de banner
      si banner = 1
        imprimir probabilidades de banner 1
      si banner = 2
        imprimir probabilidades de banner 2
      si banner = 3
        imprimir probabilidades de banner 3
  si funcion = 3
    pedir primogemas
    pedir polvo estelar
    pedir brillo estelar 
    destinos primos = primogemas / 160
    destinos polvo = polvo estelar / 75
    destinos brillo = brillo estelar / 5
    destinos totales = destinos primos + destinos polvo + destinos brillo
    imprimir destinos totales
    
