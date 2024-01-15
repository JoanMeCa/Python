import pygame
from pygame.sprite import Sprite
import math

class Planeta(Sprite):
    def __init__(self):
        super().__init__()

        # Imagen de planeta
        # Cargar la imagen original del planeta
        self.original_image = pygame.image.load("planet_250.png")

        # Escalar la imagen a la mitad
        self.image = pygame.transform.scale(self.original_image, (250,250))

        # Obtener el rectángulo de la imagen
        self.rect = self.image.get_rect()

        # Centrar el rectángulo en el centro de la pantalla
        ANCHO, ALTO = 1000, 800
        self.rect.centerx = ANCHO // 2
        self.rect.centery = ALTO // 2
        self.angulo_rotacion = 0

    def rotar_izquierda(self):
        # Rotar el planeta hacia la izquierda
        self.angulo_rotacion += 0.5  # Ajusta el ángulo según sea necesarios
        self.rotar_imagen()

    def rotar_derecha(self):
        # Rotar el planeta hacia la derecha
        self.angulo_rotacion -= 0.5  # Ajusta el ángulo según sea necesario
        self.rotar_imagen()

    def rotar_imagen(self):
        # Rotar la imagen y ajustar el rectángulo
        self.image = pygame.transform.rotate(self.original_image, self.angulo_rotacion)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        # Actualizar la posición o realizar otras operaciones según las teclas presionadas
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_a]:
            self.rotar_izquierda()

        if teclas[pygame.K_d]:
            self.rotar_derecha()

class Torreta(Sprite):
    def __init__(self, planeta, angulo_inicial, todos_los_sprites):
        super().__init__()

        # Cargar la imagen original de la torreta
        self.image = pygame.image.load("turret.png")

        # Obtener el rectángulo de la imagen
        self.rect = self.image.get_rect()

        # Establecer la rotación inicial
        self.angulo_rotacion_inicial = angulo_inicial
        self.angulo_rotacion_actual = (angulo_inicial) % 360  # Ajustar la rotación inicial según la descripción
        self.rotar_imagen()

        # Ajustar la posición y el centro de la torreta en relación con el centro del planeta
        self.posicionar_en_borde_planeta(planeta)
        self.distancia_al_centro = max(planeta.rect.width, planeta.rect.height) // 2
        self.planeta = planeta
        self.todos_los_sprites = todos_los_sprites
        self.tiempo_ultimo_disparo = 0
        self.intervalo_disparo = 500

    def posicionar_en_borde_planeta(self, planeta):
        # Calcular las coordenadas en el borde del planeta según el ángulo
        radio_planeta = max(planeta.rect.width, planeta.rect.height) // 2
        x_borde = planeta.rect.centerx + int(radio_planeta * math.cos(math.radians(self.angulo_rotacion_inicial)))
        y_borde = planeta.rect.centery - int(radio_planeta * math.sin(math.radians(self.angulo_rotacion_inicial)))

        # Establecer la posición y el centro de la torreta en el punto calculado
        self.rect.center = (x_borde, y_borde)

    def rotar_imagen(self):
        # Rotar la imagen según el ángulo de rotación actual
        self.image = pygame.transform.rotate(pygame.image.load("turret.png"), self.angulo_rotacion_actual)
        self.rect = self.image.get_rect(center=self.rect.center)
    def disparar(self):
        tiempo_actual = pygame.time.get_ticks()

        # Verifica si ha pasado suficiente tiempo desde el último disparo
        if tiempo_actual - self.tiempo_ultimo_disparo > self.intervalo_disparo:
            # Crear un proyectil desde el centro de la torreta hacia la dirección que está mirando
            proyectil = Proyectil(self.rect.centerx, self.rect.centery, self.angulo_rotacion_actual)

            # Agregar el proyectil al grupo de sprites
            self.todos_los_sprites.add(proyectil)

            # Actualizar el tiempo del último disparo
            self.tiempo_ultimo_disparo = tiempo_actual

    def update(self):
     # Seguir la rotación del planeta
        self.angulo_rotacion_actual = (self.angulo_rotacion_inicial + self.planeta.angulo_rotacion) % 360
        self.rotar_imagen()
        self.posicionar_en_borde_planeta(self.planeta)

        # Ajustar la posición de la torreta en relación con el centro del planeta
        self.rect.centerx = self.planeta.rect.centerx + int(self.distancia_al_centro * math.cos(math.radians(self.angulo_rotacion_actual)))
        self.rect.centery = self.planeta.rect.centery - int(self.distancia_al_centro * math.sin(math.radians(self.angulo_rotacion_actual)))
        
class Proyectil(Sprite):
    def __init__(self, x, y, angulo_torreta):
        super().__init__()

        # Cargar la imagen original del proyectil
        self.original_image = pygame.image.load("proyectil.png")

        # Obtener el rectángulo de la imagen
        self.rect = self.original_image.get_rect()

        # Establecer la posición inicial y el ángulo de disparo
        self.rect.centerx = x
        self.rect.centery = y

        # Ángulo de la torreta en el momento del disparo
        self.angulo_torreta = angulo_torreta

        # Velocidad del proyectil
        self.velocidad = 5

        # Calcular la velocidad en las componentes x e y según el ángulo de la torreta
        self.velocidad_x = self.velocidad * math.cos(math.radians(self.angulo_torreta))
        self.velocidad_y = -self.velocidad * math.sin(math.radians(self.angulo_torreta))

        # Inicializar la imagen rotada
        self.rotar_imagen()

    def rotar_imagen(self):
        # Rotar la imagen según el ángulo de rotación actual
        self.image = pygame.transform.rotate(self.original_image, self.angulo_torreta + 180)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        # Mover el proyectil en la dirección del ángulo
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Rotar la imagen durante la actualización
        self.rotar_imagen()