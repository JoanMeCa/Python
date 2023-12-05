import pygame
from objetos import Cat

pygame.init()

#Tamaño Pantalla

pantalla = pygame.display.set_mode((1200, 600))

#Titulo

pygame.display.set_caption("Armada Alien Invasion Mexican Cat Who Is Really Just A Cat With A Sombrero And Maracas Defending His Chimoles From Aliens The Videogame")

#Jugador

cat = Cat()

# Epilepsia Simulator

colores = [
    (255, 0, 0),    # Rojo
    (255, 165, 0),  # Naranja
    (255, 255, 0),  # Amarillo
    (0, 255, 0),    # Verde
    (0, 0, 255),    # Azul
    (75, 0, 130),   # Índigo
    (128, 0, 128)   # Violeta
]
#Tiempo/Ticks

cambio_color_tiempo = 10  # Epilepsia block
cambio_imagen_tiempo = 150  # Jugador
tiempo_anterior_color = pygame.time.get_ticks() #Cosas de epilepsia
tiempo_anterior_imagen = pygame.time.get_ticks() #Cosas de frames
image_index = 0
indice_color_actual = 0
clock = pygame.time.Clock()

salir = False

#Juego

while not salir:
    pantalla.fill((0,0,0)) #Color pantalla
    # El juego
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True

    #Movimiento        
            
    teclas = pygame.key.get_pressed()
    cat.mover(teclas)

    # Cambio de color epileptico
    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - tiempo_anterior_color >= cambio_color_tiempo:
        indice_color_actual = (indice_color_actual + 1) % len(colores)
        tiempo_anterior_color = tiempo_actual

    #Rectangulo epileptico

    rect_width = 80
    rect_height = 80
    rect_color = (colores[indice_color_actual])
    rect = pygame.Rect((400 - rect_width // 2, 300 - rect_height // 2, rect_width, rect_height))
    pygame.draw.rect(pantalla, rect_color, rect)
    
    #Jugador
    
    cat.cambiar_imagen(tiempo_actual, cambio_imagen_tiempo)

    cat.dibujar()

    # No idea really

    pygame.display.flip()

    clock.tick(30)

pygame.quit()