import pygame

class Cat:
    def __init__(self):
        self.posiz = 300
        self.postop = 507

        self.derecha = pygame.image.load("derecha.png")
        self.izquierda = pygame.image.load("izquierda.png")

        scaled_width = 100
        scaled_height = 93
        self.derecha = pygame.transform.scale(self.derecha, (scaled_width, scaled_height))
        self.izquierda = pygame.transform.scale(self.izquierda, (scaled_width, scaled_height))
        self.images = [self.derecha, self.izquierda]

        self.image_index = 0
        self.tiempo_anterior_imagen = 0  # Inicializar a 0

    def mover(self, teclas):
        pantalla = pygame.display.get_surface()
        limite = pantalla.get_width() - self.izquierda.get_width()
        self.posiz = min(self.posiz, limite)
        if teclas[pygame.K_a] and self.posiz > 0:
            self.posiz -= 20
        if teclas[pygame.K_d]:
            self.posiz = min(self.posiz + 20, limite)

    def dibujar(self, pantalla=None):
        if pantalla is None:
            pantalla = pygame.display.get_surface()
        pantalla.blit(self.images[self.image_index], (self.posiz, self.postop))

    def cambiar_imagen(self, tiempo_actual, cambio_imagen_tiempo):
        if tiempo_actual - self.tiempo_anterior_imagen >= cambio_imagen_tiempo:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.tiempo_anterior_imagen = tiempo_actual