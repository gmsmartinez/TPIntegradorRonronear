from Usuario import Usuario
from Bots import Terminator

print("")
print("    ###################################")
print("    #                                 #")
print("    #   Hola!! Bienvenidos a          #")
print("    #        PdpTwitter!!             #")
print("    #                                 #")
print("    ###################################")


def start_tuitear():
    start = None
    while start != "S":
        start = input("¿Queres ingresar tu usuario y contrasenia?: [S/N] ")
        start = start.upper()
        if start == "N":
            print("En serio?? Somos mejores que Facebook!!!")
            exit()
        if start == "S":
            print("Bien!! Vamos a tuitear!!!")
start_tuitear()

usuario = Usuario(input("Bienvenido a Pdptwitter, por favor ingrese su nombre de usuario: "))

# Mejorar este codigo
while (True):

    print("Bienvenido " + usuario.nombre + " a Pdptwitter, ¿que desea hacer?")
    print("1. Ver mis tweets")
    print("2. Escribir un tweet")
    print("3. Ver mis Menciones")
    print("4. Cerrar Sesion")
    
    opcion = int(input())
    if opcion == 1:

        print("Estos son tus tweets: ")
        for tweet in usuario.mensajes:
            print(tweet)

    elif opcion == 2:

        respuesta = usuario.twittear()
        print(respuesta)

    

    elif opcion == 3:
        
        print("De cual usuario arrobado queres ver las menciones?")
        if tweet in usuarioMaria.twittear:
            print(tweet)
        elif tweet in usuarioJuan.twittear:
            print(tweet)
        elif tweet in usuarioPedro.twittear:
            print(tweet)
        
        break

    elif opcion == 4:
        break



    else:
        print("Ingrese una opcion valida")



Terminator.guardarTweets(usuario.nombre, usuario.verMensajes())
