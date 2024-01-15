import pygame
from pygame.locals import QUIT, KEYDOWN
from objetos import Planeta, Torreta, Proyectil
pygame.init()

# Pantalla

NEGRO = (0, 0, 0)
ANCHO, ALTO = 1000, 800
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Lovers In A Dangerous Planet")
todos_los_sprites = pygame.sprite.Group()

#Clases importadas

planet = Planeta()
turret_South = Torreta(planet, 180, todos_los_sprites)
turret_East = Torreta(planet, 90, todos_los_sprites)
turret_West = Torreta(planet, 270, todos_los_sprites)
turret_North = Torreta(planet, 0, todos_los_sprites)
todos_los_sprites.add(turret_East, turret_North, turret_South, turret_West, planet)

#Bucle principal

jugar = True
while jugar:
    teclas_presionadas = pygame.key.get_pressed()
    for evento in pygame.event.get():
        if evento.type == QUIT:
            jugar = False
        elif evento.type == KEYDOWN:
            teclas_presionadas = pygame.key.get_pressed()
            planet.update()
    

    if teclas_presionadas[pygame.K_SPACE]:
        turret_North.disparar()
        turret_East.disparar()
        turret_South.disparar()
        turret_West.disparar()
        
    #Actualizar los sprites    
    todos_los_sprites.update()
    
    #Dibujar los elementos
    pantalla.fill(NEGRO)
    todos_los_sprites.draw(pantalla)
    pygame.display.flip()

pygame.quit()    