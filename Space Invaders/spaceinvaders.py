import pygame
from objetos import Cat, Background, Proyectil

#Game ON

pygame.init()

#Tamaño Pantalla

tamañopantalla = (1000,600) #Controla el tamaño de la pantalla
pantalla = pygame.display.set_mode(tamañopantalla)

#Titulo

pygame.display.set_caption("Armada Alien Invasion Mexican Cat Who Is Really Just A Cat With A Sombrero And Maracas Defending His Chimoles From Aliens The Videogame")

#Tiempo/Ticks

velocidad_fondo = 15    #Wow, me pregunto que hará esto
cambio_imagen_tiempo = 150  # Cada cuantos frames cambia el sprite del jugador
tiempo_anterior_imagen = pygame.time.get_ticks() #Cosas de frames
image_index = 0 #Mas cosas de frames
clock = pygame.time.Clock() #Reloj, xd
FPS = 30 #Frames por segundo (No cambiar, juego diseñado a 30 FPS)

#Clases Importadas

cat = Cat((450,505))
background = Background(velocidad_fondo)

# Sprites

todos_los_sprites = pygame.sprite.Group()
proyectiles = pygame.sprite.Group()
todos_los_sprites.add(cat)

#Juego

salir = False
while not salir:
    pantalla.fill((0,0,0))
    background.actualizar()
    background.dibujar(pantalla)
    # El juego
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            cat.activar_disparo()  # Activar el disparo cuando se pulsa la barra espaciadora

    #Movimiento        
            
    teclas = pygame.key.get_pressed()

    #Tiempo

    tiempo_actual = pygame.time.get_ticks()
    
    # Crear un proyectil cuando se pulsa la tecla de espacio
    if teclas[pygame.K_SPACE] and cat.puede_disparar:
        proyectil = Proyectil(cat.rect.x + cat.derecha.get_width() // 2, cat.rect.y)
        todos_los_sprites.add(proyectil)
        proyectiles.add(proyectil)
        cat.desactivar_disparo()  # Desactivar el disparo cuando se presiona la barra espaciadora

    todos_los_sprites.update(teclas, tiempo_actual, cambio_imagen_tiempo)
    todos_los_sprites.draw(pantalla)
    # No idea really

    pygame.display.flip()

    #FPS

    clock.tick(FPS)

pygame.quit()