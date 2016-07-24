# coding: utf-8
import pilasengine
import os
import random

pilas = pilasengine.iniciar()
fondojuego=pilas.fondos.Fondo()
fondojuego.imagen=pilas.imagenes.cargar("fondojuego.jpg")
fondojuego=True
class Burbuja2(pilasengine.actores.Actor):

    def iniciar(self):
          self.imagen = "burbuja2.png"
 
burbuja2=Burbuja2(pilas)
class Nave(pilasengine.actores.Actor):

    def iniciar(self):
          self.imagen = "nave.png"
 
nave=Nave(pilas)
class Burbuja3(pilasengine.actores.Actor):

    def iniciar(self):
          self.imagen = "burbuja3.png"
          burbuja3.decir(u"¡oh, no, humanos!")
burbuja3=Burbuja3(pilas)            
burbuja3.x= 290
class Burbuja4(pilasengine.actores.Actor):

    def iniciar(self):
          self.imagen = "burbuja4.png"
  
burbuja4=Burbuja4(pilas)            
burbuja4.x= -290
class Burbuja5(pilasengine.actores.Actor):

    def iniciar(self):
          self.imagen = "burbuja5.png"
  
burbuja5=Burbuja5(pilas)            
burbuja5.x= 0
burbuja5.y=185

def comenzar_juego():
    menu.eliminar()
    puntaje = pilas.actores.Puntaje(+200, +200, color=pilas.colores.azul)
    
    class Crear_Aceituna(pilasengine.actores.Aceituna):       
          
        def iniciar(self):
            self.aprender( pilas.habilidades.PuedeExplotarConHumo )
            self.x = pilas.azar(-200, 200)
            self.y = 290
            self.velocidad = pilas.azar(10, 40) / 10.0

        def actualizar(self):
            self.rotacion += 10
            self.y -= self.velocidad

            # Elimina el objeto cuando sale de la pantalla.
            if self.y < -300:
                self.eliminar()
                  
    class Crear_Bomba(pilasengine.actores.Bomba):
        
        def iniciar(self):
            self.aprender( pilas.habilidades.PuedeExplotar)
            self.x = pilas.azar(-400, 400)
            self.y = 250
            self.velocidad = pilas.azar(10, 20) / 10.0

        def actualizar(self):
            self.rotacion += 12
            self.y -= self.velocidad

            # Elimina el objeto cuando sale de la pantalla.
            if self.y < -500:
                self.eliminar()
                
    class Crear_Manzana(pilasengine.actores.Manzana):
        
        def iniciar(self):

            self.aprender( pilas.habilidades.PuedeExplotar)
            self.x = pilas.azar(-200, 200)
            self.y = 250
            self.velocidad = pilas.azar(10, 30) / 10.0
            self.escala = 0.5
        def actualizar(self):
            self.rotacion += 8
            self.y -= self.velocidad

            # Elimina el objeto cuando sale de la pantalla.
            if self.y < -500:
                self.eliminar()

    class disparos():
        
        def disparo_doble():
            nave.aprender(pilas.habilidades.Disparar,
            municion=pilas.municion.BalaDoble,
            offset_disparo=(0, 30))
                
    fondo = pilas.fondos.Galaxia(dy=-5)
    
    enemigos = pilas.actores.Grupo()
    

    def Activar_Enemigo():
        actor =Crear_Aceituna(pilas)
        enemigos.agregar(actor)
        actor = Crear_Bomba(pilas)
        enemigos.agregar(actor)
        actor =Crear_Manzana(pilas)
        enemigos.agregar(actor)
        
            
    pilas.tareas.siempre(0.50, Activar_Enemigo)
    nave = pilas.actores.Nave(y = -200)
    nave.aprender(pilas.habilidades.LimitadoABordesDePantalla)
    nave.definir_enemigos(enemigos, puntaje.aumentar)
    pilas.colisiones.agregar(nave, enemigos, nave.eliminar)

    pilas.avisar("Dispara co ESPACIO y muevete con las FLECHAS del teclado...")

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
        


pilas.ejecutar()
