from Usuario import Usuario
from Bots import Terminator

usuario = Usuario(input("Bienvenido a Pdptwitter, por favor ingrese su nombre de usuario: "))

# Mejorar este codigo
while (True):

    print("Bienvenido " + usuario.nombre + " a Pdptwitter, ¿que desea hacer?")
    print("1. Ver mis tweets")
    print("2. Escribir un tweet")
    print("3. Cerrar sesion")
    
    opcion = int(input())
    if opcion == 1:

        print("Estos son tus tweets: ")
        for tweet in usuario.mensajes:
            print(tweet)

    elif opcion == 2:

        respuesta = usuario.twittear()
        print(respuesta)

    elif opcion == 3:
        break

    else:
        print("Ingrese una opcion valida")


Terminator.guardarTweets(usuario.nombre, usuario.ver_mensajes())