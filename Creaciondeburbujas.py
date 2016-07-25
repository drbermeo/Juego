#TRABAJO GRUPAL 
# Integrantes: Diana Bermeo-Ximena Briceño
# Importar librerias
import pilasengine
import os
import random
#Linea de codigo para agregar musica
sonido1 = pilas.musica.cargar('burbujita.mp3')
sonido1.reproducir()
#Linea de codigo para poder iniciar pilas
pilas = pilasengine.iniciar()
# Parte del menu , donde se realizaa todas las lineas dde coigo escritas si el usuario elige comenzar_juego
def comenzar_juego():
    #Cuando comienza el juego el menu, desaparece
        menu.eliminar()
    # La nave se hace mas pequeña
        nave.escala= 0.1
    # Se cambia el fondo del juego
        fondo=pilas.fondos.Galaxia()
        pilas.avisar('Gana puntos solo con las burbujas blancas')
#Creando una clase llamada Estado para la posicion de la nave
class Estado:

    
    def __init__(self, nave):
        self.nave = nave
        self.iniciar()
       
    def iniciar(self):
        pass
        
  #Clase que ejecutara lineas de codigo cuando la nave pierda  
class Perdiendo(Estado):

    def iniciar(self):
        self.nave.definir_animacion([0])
        self.nave.centro = ('centro', 'centro')
        self.velocidad = -2

    def actualizar(self):
        self.nave.rotacion += 7
        self.nave.escala += 0.01
        self.nave.x += self.velocidad
        self.velocidad += 0.2
        self.nave.y -= 1

#Creando una clase para el actor nave
class Nave(pilasengine.actores.Actor):

    def iniciar(self):
        # Se crea un nuevo actor  de una imagen y se lo personaliza
        self.imagen = "combatiente.png"
        self.definir_animacion([0])
        self.centro = (140, 59)
        self.radio_de_colision = 40
        self.x = -170
        self.estado = Ingresando(self)
        self.contador = 0
        self.escala = 0.1
    def definir_animacion(self, cuadros):
        self.paso = 0
        self.contador = 0
        self.cuadros = cuadros

    def actualizar(self):
        self.estado.actualizar()
        self.actualizar_animacion()

    def actualizar_animacion(self):
        self.contador += 0.2

        if (self.contador > 1):
            self.contador = 0
            self.paso += 1

           
#Lineas de codigo para cuando la nave pierda
    def perder(self):
        self.estado = Perdiendo(self)
        t = pilas.actores.Texto("Game Over")
        sonido1.detener()
        sonido2=pilas.musica.cargar('game.mp3')
        sonido2.reproducir()
        t.escala = 0
        t.escala = [3], 0.5
#Clase que sirve para crear la burbuja roja
class Enemigo(pilasengine.actores.Actor):

    def iniciar(self):
        
        self.imagen = "roja.png"
        self.izquierda = 320
        self.escala = 0.5
        self.y = random.randint(-210, 210)
    
    def actualizar(self):
        self.x -= 5
        pilasengine.actores.Actor.actualizar(self)

class Burbuja(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = 'blanca.png'
        self.escala = 0.5
        self.izquierda = 320
        self.y = random.randint(-210, 210)
        
       

    def actualizar(self):
        self.izquierda -= 5

        if self.derecha < -320:
            self.eliminar()




pilas = pilasengine.iniciar(capturar_errores=False)

 # Linea de codigo paue crea el nuevo fondo  
fondojuego=pilas.fondos.Fondo()
fondojuego.imagen=pilas.imagenes.cargar("fondojuego.jpg")
fondojuego=True
actor=Enemigo(pilas)
# Linea de codigo que cuenta los puntajes de las burbujas blancas
puntos = pilas.actores.Puntaje(200,200, color= pilas.colores.blanco)
nave = Nave(pilas)
items = []
enemigos = []

def crear_item():
    un_item = Burbuja(pilas)
    items.append(un_item)
    return True

pilas.tareas.agregar(2, crear_item)


def cuanto_toca_item(v, i):
    i.eliminar()
    puntos.aumentar(1)
    puntos.escala = 2
    puntos.escala = [1], 0.2
    puntos.rotacion = random.randint(30, 60)
    puntos.rotacion = [0], 0.2

pilas.colisiones.agregar(nave, items, cuanto_toca_item)


def crear_enemigo():
    un_enemigo = Enemigo(pilas)
    enemigos.append(un_enemigo)
    return True

pilas.tareas.agregar(3.3, crear_enemigo)


def cuanto_toca_enemigo(nave, enemigo):
    nave.perder()
    
   

pilas.colisiones.agregar(nave, enemigos, cuanto_toca_enemigo)


def salir():
        
        opciones = pilas.interfaz.ListaSeleccion(['Score'], salir_del_juego)
        opciones.x = +200
        opciones.y = +200    
        pilas.eliminar()
#Si elige la opcion salir el juego terminara
    # El sonido se detedra
def salir_del_juego():
    
    pilas.terminar()
    sonido1.detener() 

#Codigo del menu
menu=pilas.actores.Menu([
        ('Comenzar Juego', comenzar_juego),
        ('Salir', salir_del_juego),
        ])
pilas.avisar('Bienvenidos a Whitebubble')
nave.escala = -0.1

pilas.ejecutar()
