import pygame
from objetos import Cat
from objetos import Background
from objetos import Proyectil

pygame.init()

#Tamaño Pantalla

pantalla = pygame.display.set_mode((1000, 600))

#Titulo

pygame.display.set_caption("Armada Alien Invasion Mexican Cat Who Is Really Just A Cat With A Sombrero And Maracas Defending His Chimoles From Aliens The Videogame")

#Tiempo/Ticks

velocidad_fondo = 15    #Wow, me pregunto que hará esto
cambio_imagen_tiempo = 150  # Jugador
tiempo_anterior_imagen = pygame.time.get_ticks() #Cosas de frames
image_index = 0
indice_color_actual = 0
clock = pygame.time.Clock()

# Grupos de sprites
todos_los_sprites = pygame.sprite.Group()
proyectiles = pygame.sprite.Group()

salir = False

#Clases Importadas

cat = Cat()
background = Background(velocidad_fondo)

#Juego

while not salir:
    pantalla.fill((0,0,0))
    background.actualizar()
    background.dibujar(pantalla)
    # El juego
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            cat.activar_disparo()  # Activar el disparo cuando se suelta la barra espaciadora

    #Movimiento        
            
    teclas = pygame.key.get_pressed()
    cat.mover(teclas)

    #Tiempo

    tiempo_actual = pygame.time.get_ticks()
    
    #Jugador
    
    cat.cambiar_imagen(tiempo_actual, cambio_imagen_tiempo)

    cat.dibujar()
    
    # Crear un proyectil cuando se pulsa la tecla de espacio
    if teclas[pygame.K_SPACE] and cat.puede_disparar:
        proyectil = Proyectil(cat.posiz + cat.derecha.get_width() // 2, cat.postop)
        todos_los_sprites.add(proyectil)
        proyectiles.add(proyectil)
        cat.desactivar_disparo()  # Desactivar el disparo cuando se presiona la barra espaciadora

    todos_los_sprites.update()
    todos_los_sprites.draw(pantalla)
    # No idea really

    pygame.display.flip()

    clock.tick(30)

pygame.quit()