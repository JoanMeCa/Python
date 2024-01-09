import pygame
import pygame_menu
from objetos import Cat, Background, Enemigo

pygame.init()

#Tamaño Pantalla

tamañopantalla = (1000,600) #Controla el tamaño de la pantalla
pantalla = pygame.display.set_mode(tamañopantalla)
pygame.display.set_caption("Armada Alien Invasion Mexican Cat Who Is Really Just A Cat With A Sombrero And Maracas Defending His Chimoles From Aliens The Videogame")

def start_the_game():
    global salir
    salir = False
    #Tiempo/Ticks
    velocidad_fondo = 15    #Wow, me pregunto que hará esto
    cambio_imagen_tiempo = 150  # Cada cuantos frames cambia el sprite del jugador
    tiempo_anterior_imagen = pygame.time.get_ticks() #Cosas de frames
    image_index = 0 #Mas cosas de frames
    clock = pygame.time.Clock() #Reloj, xd
    FPS = 30 #Frames por segundo (No cambiar, juego diseñado a 30 FPS)
    contador_frames = 0 #Contador de frames para enemigos
    frames_enemigo = 15 #Cada cuantos frames aparece un enemigo   

    #Clases Importadas

    cat = Cat((450,505)) #Posicion Inical Jugador
    background = Background(velocidad_fondo)

    # Sprites

    todos_los_sprites = pygame.sprite.Group()
    proyectiles = pygame.sprite.Group() #Más que los proyectiles, aquí está la mascara de colisión de los mismos
    enemigos = pygame.sprite.Group()  # Grupo para los enemigos
    todos_los_sprites.add(cat)
    
    # El juego
    
    while not salir:
        pantalla.fill((0,0,0))
        background.update()
        background.draw(pantalla)
        teclas = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                cat.activar_disparo()  # Activar el disparo cuando se suelta la barra espaciadora

        #Controles
        
        cat.disparar(teclas, proyectiles, todos_los_sprites)

        #Tiempo

        tiempo_actual = pygame.time.get_ticks()
        
        #Actualizar los sprites
        
        todos_los_sprites.update(teclas, tiempo_actual, cambio_imagen_tiempo, enemigos, proyectiles=proyectiles)
        
        #Spawneo Enemigos
        
        contador_frames += 1
        if contador_frames >= frames_enemigo:
            contador_frames = 0
            nuevo_enemigo = Enemigo ((-200, 0))  # Posición inicial del nuevo enemigo
            todos_los_sprites.add(nuevo_enemigo)
            enemigos.add(nuevo_enemigo)
            nuevo_enemigo = Enemigo((1000, -100))  # Posición inicial del nuevo enemigo
            todos_los_sprites.add(nuevo_enemigo)
            enemigos.add(nuevo_enemigo)

        colision_enemigo = pygame.sprite.spritecollide(cat, enemigos, False, pygame.sprite.collide_mask)
        if colision_enemigo:
            cat.kill()  # Eliminar al gato si hay colisión con algún enemigo
            salir = True
        
        # No idea really
        todos_los_sprites.draw(pantalla)
        pygame.display.flip()

        #FPS

        clock.tick(FPS)


    
#Menu
menu = pygame_menu.Menu("It's Morbin' Time", 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(pantalla)


# Menu
# main_menu = True
# while main_menu:
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT:
#             main_menu = False
#             salir = True
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
#             main_menu = False

#     pantalla.fill((0, 0, 0))
#     background.update()
#     background.draw(pantalla)
#     menu.mainloop(pantalla, events)

#     pygame.display.flip()
pygame.quit()