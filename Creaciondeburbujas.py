# coding: utf-8
import pilasengine
import os
import random

pilas = pilasengine.iniciar()
fondojuego=pilas.fondos.Fondo()
fondojuego.imagen=pilas.imagenes.cargar("fondojuego.jpg")
fondojuego=True

def comenzar_juego():
    menu.eliminar()
    puntaje = pilas.actores.Puntaje(+200, +200, color=pilas.colores.azul)
class Bur_azul(pilasengine.actores.Actor):

    def iniciar(self):
          self.imagen = "azul.png"
class Bur_roja(pilasengine.actores.Actor):

    def iniciar(self):
          self.imagen = "roja.png"
class Bur_blanca(pilasengine.actores.Actor):

    def iniciar(self):
          self.imagen = "blanca.png"
class Bur_negra(pilasengine.actores.Actor):

    def iniciar(self):
          self.imagen = "negra.png"
class Nave(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "nave.png"
        
        self.x += 0
        self.y   -= 220
        
    def dar_vuelta(self):
        self.rotacion = [180]
    
    def actualizar(self):
        if pilas.control.izquierda:
            self.x -= 5
            
            self.espejado = True
        if pilas.control.derecha:
            self.x += 5
           
            self.espejado = False
    def disparo_doble():
            nave.aprender(pilas.habilidades.Disparar,
            municion=pilas.municion.BalaDoble,
            offset_disparo=(0, 30))
                
  

def salir():
    pilas.terminar()
    
    opciones = pilas.interfaz.ListaSeleccion(['Score'], salir)
    opciones.x = +195
    opciones.y = +178

def salir_del_juego():
    pilas.terminar()


menu=pilas.actores.Menu([
        
        ('Comenzar Juego', comenzar_juego),
        ('Salir', salir_del_juego),
        ])
        

 
  
alien=Nave(pilas)



pilas.ejecutar()