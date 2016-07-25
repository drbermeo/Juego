# coding: utf-8
import pilasengine
import pilasengine
import os
import random
sonido1 = pilas.musica.cargar('burbujita.mp3')
sonido1.reproducir()
  

class Estado:
    
    
    def __init__(self, nave):
        self.nave = nave
        self.iniciar()
       
    def iniciar(self):
        pass
        
      

class Ingresando(Estado):

    def iniciar(self):
        self.nave.definir_animacion([3, 4])
        self.contador = 0
        self.nave.x = -200
        self.nave.x = [-300], 0.5
       
    def actualizar(self):
        self.contador += 1

        if self.contador > 50:
            self.nave.estado = Volando(self.nave)

class Volando(Estado):

    def iniciar(self):
        self.nave.definir_animacion([3, 4])

    def actualizar(self):
        velocidad = 5

        if pilas.escena.control.arriba:
            self.nave.y += velocidad
        elif pilas.escena.control.abajo:
            self.nave.y -= velocidad

        if self.nave.y > 210:
            self.nave.y = 210
        elif self.nave.y < -210:
            self.nave.y = -210


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


class Nave(pilasengine.actores.Actor):

    def iniciar(self):
        
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

            if self.paso >= len(self.cuadros):
                self.paso = 0

        self.imagen.definir_cuadro(self.cuadros[self.paso])

    def perder(self):
        self.estado = Perdiendo(self)
        t = pilas.actores.Texto("Game Over")
        sonido1.detener()
        sonido2=pilas.musica.cargar('game.mp3')
        sonido2.reproducir()
        t.escala = 0
        t.escala = [1], 0.5

class Enemigo(pilasengine.actores.Actor):

    def iniciar(self):
        
        self.imagen = "roja.png"
        self.izquierda = 320
        self.escala = 0.5
        self.y = random.randint(-210, 210)
    
    def actualizar(self):
        self.x -= 5
        pilasengine.actores.Actor.actualizar(self)

class Item(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = 'blanca.png'
        self.escala = 0.5
        self.izquierda = 320
        self.y = random.randint(-210, 210)
        self.decir("Hola") 
       

    def actualizar(self):
        self.izquierda -= 5

        if self.derecha < -320:
            self.eliminar()




pilas = pilasengine.iniciar(capturar_errores=False)

   
fondojuego=pilas.fondos.Galaxia()
actor=Enemigo(pilas)

puntos = pilas.actores.Puntaje(x=-290, y=210)
nave = Nave(pilas)
items = []
enemigos = []

def crear_item():
    un_item = Item(pilas)
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

         
  
         
pilas.ejecutar()
