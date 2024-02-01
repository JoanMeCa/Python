import pygame
import pygame.time
import pygame_menu
from pygame.locals import QUIT, KEYDOWN
from objetos import Planeta, Torreta, Proyectil, Meteorito, Background
pygame.init()

# Pantalla

ANCHO, ALTO = 1000, 800
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Lovers In A Dangerous Planet")
todos_los_sprites = pygame.sprite.Group()
todos_los_proyectiles = pygame.sprite.Group()

nivel_dificultad = 1
#Clases importadas
fondo = Background((ANCHO, ALTO))
planet = Planeta()
turret_North = Torreta(planet, 0, todos_los_proyectiles)
turret_South = Torreta(planet, 180, todos_los_proyectiles)
turret_East = Torreta(planet, 90, todos_los_proyectiles)
turret_West = Torreta(planet, 270, todos_los_proyectiles)
meteoritos = pygame.sprite.Group()
    
def set_difficulty(value, difficulty):
    global nivel_dificultad
    nivel_dificultad = difficulty
    pass

def reiniciar_juego():
    global jugar, nivel_dificultad
    planet.puntos_de_vida = 3
    todos_los_proyectiles.empty()
    meteoritos.empty()

def start_the_game():
    global jugar, nivel_dificultad
    reiniciar_juego()
    velocidad_meteoritos = 2
    tiempo_transcurrido = 0
    intervalo_meteorito = 1000  # 1000 milisegundos = 1 segundo
    reloj = pygame.time.Clock()
    puntuacion = 0
    tiempo_ultima_actualizacion = pygame.time.get_ticks()
    fuente = pygame.font.Font(None, 36)
    
    if nivel_dificultad == 1:
        planet.angulo = 0.5
        turret_North.kill()
        turret_South.kill()
        turret_East.kill()
        turret_West.kill()
        planet.kill()
        todos_los_sprites.add(turret_North, turret_South, turret_East, turret_West, planet)
        turret_North.intervalo_disparo = 500
        intervalo_meteorito = 800
    
    if nivel_dificultad == 2:
        # Ajusta la velocidad de rotación del planeta
        planet.angulo = 1.5
        turret_North.kill()
        turret_South.kill()
        turret_East.kill()
        turret_West.kill()
        planet.kill()
        todos_los_sprites.add(turret_North, planet)
        turret_North.intervalo_disparo = 300
        intervalo_meteorito = 1000
    
    #Juego
    
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
        if nivel_dificultad == 1:
            if teclas_presionadas[pygame.K_SPACE]:
                turret_North.disparar()
                turret_East.disparar()
                turret_South.disparar()
                turret_West.disparar()
        elif nivel_dificultad == 2:
            if teclas_presionadas[pygame.K_SPACE]:
                turret_North.disparar()
                
        #Actualizar los sprites    
        todos_los_sprites.update()
        todos_los_proyectiles.update()
        meteoritos.update(planet, velocidad_meteoritos)
        
        for proyectil in todos_los_proyectiles:
            colisiones = pygame.sprite.groupcollide(meteoritos, todos_los_proyectiles, True, True, pygame.sprite.collide_mask)
            for meteorito in colisiones:
                puntuacion += 50
            
        # Verificar colisiones con los meteoritos
        colisiones = pygame.sprite.spritecollide(planet, meteoritos, True, pygame.sprite.collide_mask)
        for meteorito in colisiones:
            planet.puntos_de_vida -= 1
            if planet.puntos_de_vida <= 0:
                # Aquí puedes agregar acciones adicionales cuando se quedan sin puntos de vida
                jugar = False  # Terminar el juego si se quedan sin puntos de vida
        

        
        #Dibujar los elementos
        pantalla.blit(fondo.image, fondo.rect)
        todos_los_sprites.draw(pantalla)
        todos_los_proyectiles.draw(pantalla)
        meteoritos.draw(pantalla)
        
        # Mostrar la puntuación en la esquina inferior derecha
        texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, (255, 255, 255))
        pantalla.blit(texto_puntuacion, (ANCHO - 220, ALTO - 40))
        
        texto_vida = fuente.render(f"Vida: {planet.puntos_de_vida}", True, (255, 255, 255))
        pantalla.blit(texto_vida, (20, 20))
        
        pygame.display.flip()
    pass
    
    
# Crear menú
menu = pygame_menu.Menu('Planet Defender', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
menu.add.selector('Dificultad :', [('Normal', 1), ('Díficil', 2)], onchange=set_difficulty)
menu.add.button('Jugar', start_the_game)
menu.add.button('Salir', pygame_menu.events.EXIT)

# Bucle principal del menú
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()

    # Actualizar y dibujar el menú
    menu.mainloop(surface=pantalla)

    # Actualizar la pantalla
    pygame.display.flip() 