import pygame

class Cat:
    def __init__(self):
        self.posiz = 300
        self.postop = 507

        self.derecha = pygame.image.load("derecha.png")
        self.izquierda = pygame.image.load("izquierda.png")
        
        self.puede_disparar = True  # Nuevo atributo para controlar si puede disparar
        
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
    def puede_disparar(self):
        return self.puede_disparar

    def desactivar_disparo(self):
        self.puede_disparar = False

    def activar_disparo(self):
        self.puede_disparar = True
class Background:
    def __init__(self, velocidad, num_imagenes=3):
        self.imagenes = [pygame.image.load(f"background{i}.jpg") for i in range(1, num_imagenes + 1)]
        self.velocidad = velocidad
        self.num_imagenes = num_imagenes
        self.imagen_actual = 0

        # Redimensionar las imágenes al tamaño de la pantalla
        pantalla_info = pygame.display.Info()
        self.ancho_pantalla = pantalla_info.current_w
        self.alto_pantalla = pantalla_info.current_h
        self.imagenes = [pygame.transform.scale(imagen, (self.ancho_pantalla, self.alto_pantalla)) for imagen in self.imagenes]

        self.pos_y = 0  # Posición inicial en el eje Y

    def actualizar(self):
        # Actualizar la posición vertical del fondo hacia abajo
        self.pos_y += self.velocidad

        # Si la imagen actual ha pasado completamente fuera de la pantalla hacia abajo, reiniciar la posición y cambiar la imagen
        if self.pos_y >= self.alto_pantalla:
            self.pos_y = 0
            self.imagen_actual = (self.imagen_actual + 1) % self.num_imagenes

    def dibujar(self, pantalla=None):
        if pantalla is None:
            pantalla = pygame.display.get_surface()

        # Dibujar el fondo en dos posiciones para el desplazamiento continuo
        pantalla.blit(self.imagenes[self.imagen_actual], (0, self.pos_y))

        # Si la imagen se ha desplazado lo suficiente, dibujar la siguiente imagen hacia abajo
        siguiente_imagen = (self.imagen_actual + 1) % self.num_imagenes
        pantalla.blit(self.imagenes[siguiente_imagen], (0, self.pos_y - self.alto_pantalla))
class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))  # Tamaño del proyectil
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # Variables para el cambio de color constante
        self.colores = [
            (255, 0, 0),
            (255, 165, 0),
            (255, 255, 0),
            (0, 255, 0),
            (0, 0, 255),
            (75, 0, 130),
            (128, 0, 128)
        ]
        self.indice_color_actual = 0

    def update(self):
        # Actualizar la posición del proyectil hacia arriba
        self.rect.y -= 5  # Puedes ajustar la velocidad cambiando este valor

        # Cambiar de color constantemente
        self.image.fill(self.colores[self.indice_color_actual])
        self.indice_color_actual = (self.indice_color_actual + 1) % len(self.colores)

        # Eliminar el proyectil si sale de la pantalla
        if self.rect.bottom < 0:
            self.kill()