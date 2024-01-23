import pygame
import pygame.time
from pygame.locals import QUIT, KEYDOWN
from objetos import Planeta, Torreta, Proyectil, Meteorito
pygame.init()

# Pantalla

NEGRO = (0, 0, 0)
ANCHO, ALTO = 1000, 800
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Lovers In A Dangerous Planet")
todos_los_sprites = pygame.sprite.Group()
todos_los_proyectiles = pygame.sprite.Group()

#Clases importadas

planet = Planeta()
turret_South = Torreta(planet, 180, todos_los_proyectiles)
turret_East = Torreta(planet, 90, todos_los_proyectiles)
turret_West = Torreta(planet, 270, todos_los_proyectiles)
turret_North = Torreta(planet, 0, todos_los_proyectiles)
todos_los_sprites.add(turret_East, turret_North, turret_South, turret_West, planet)
meteoritos = pygame.sprite.Group()
velocidad_meteoritos = 2
tiempo_transcurrido = 0
intervalo_meteorito = 500  # 1000 milisegundos = 1 segundo
reloj = pygame.time.Clock()

#Bucle principal

jugar = True
while jugar:
    tiempo_transcurrido += reloj.tick()
    teclas_presionadas = pygame.key.get_pressed()
    for evento in pygame.event.get():
        if evento.type == QUIT:
            jugar = False
        elif evento.type == KEYDOWN:
            teclas_presionadas = pygame.key.get_pressed()
            planet.update()
    if tiempo_transcurrido > intervalo_meteorito:
        meteorito = Meteorito(planet)
        meteoritos.add(meteorito)
        tiempo_transcurrido = 0

    if teclas_presionadas[pygame.K_SPACE]:
        turret_North.disparar()
        turret_East.disparar()
        turret_South.disparar()
        turret_West.disparar()
        
    #Actualizar los sprites    
    todos_los_sprites.update()
    todos_los_proyectiles.update()
    meteoritos.update(planet, velocidad_meteoritos)
    
    for proyectil in todos_los_proyectiles:
        colisiones = pygame.sprite.groupcollide(meteoritos, todos_los_proyectiles, True, True, pygame.sprite.collide_mask)
        for meteorito in colisiones:
            # Puedes realizar acciones adicionales aquí si es necesario
            pass
    
    #Dibujar los elementos
    pantalla.fill(NEGRO)
    todos_los_sprites.draw(pantalla)
    todos_los_proyectiles.draw(pantalla)
    meteoritos.draw(pantalla)
    pygame.display.flip()

pygame.quit()    