import pygame
import random


class Cuerpo:
    def __init__(self, ventana):
        self.x = 0
        self.y = 0
        self.dir = 0
        self.ventana = ventana

    def dibujar(self):
        pygame.draw.rect(self.ventana, (255, 255, 255), (self.x, self.y, 10, 10))

    def movimiento(self):
        if self.dir == 0:
            self.x += 10
        elif self.dir == 1:
            self.x -= 10
        elif self.dir == 2:
            self.y += 10
        elif self.dir == 3:
            self.y -= 10


class Manzana:
    def __init__(self, ventana):
        self.x = random.randrange(50) * 10
        self.y = random.randrange(50) * 10
        self.ventana = ventana

    def dibujar(self):
        pygame.draw.rect(self.ventana, (255, 0, 0), (self.x, self.y, 10, 10))

    def nueva_manzana(self):
        self.x = random.randrange(50) * 10
        self.y = random.randrange(50) * 10


def refrescar(ventana):
    ventana.fill((0, 0, 0))
    comida.dibujar()
    for i in range(len(serpiente)):
        serpiente[i].dibujar()


def seguir_cabeza():
    for i in range(len(serpiente) - 1):
        serpiente[len(serpiente) - i - 1].x = serpiente[len(serpiente) - i - 2].x
        serpiente[len(serpiente) - i - 1].y = serpiente[len(serpiente) - i - 2].y


def main():
    global serpiente, comida
    ventana = pygame.display.set_mode((500, 500))
    ventana.fill((0, 0, 0))
    run = True
    comida = Manzana(ventana)
    serpiente = [Cuerpo(ventana)]
    while run:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    serpiente[0].dir = 0
                if evento.key == pygame.K_LEFT:
                    serpiente[0].dir = 1
                if evento.key == pygame.K_UP:
                    serpiente[0].dir = 3
                if evento.key == pygame.K_DOWN:
                    serpiente[0].dir = 2

        serpiente[0].movimiento()
        refrescar(ventana)
        pygame.display.update()
        pygame.time.delay(100)

        # Este segmento del código hace que si la serpiente choca contra su cuerpo, se acaba el juego
        for i in range(len(serpiente) - 2):
            if serpiente[len(serpiente) - i - 1].x == serpiente[0].x and serpiente[len(serpiente) - i - 1].y == \
                    serpiente[0].y:
                run = False

        if serpiente[0].x == comida.x and serpiente[0].y == comida.y:
            comida.nueva_manzana()
            serpiente.append(Cuerpo(ventana))
        seguir_cabeza()
        if serpiente[0].x >= 500:
            serpiente[0].x = 0
        elif serpiente[0].x < 0:
            serpiente[0].x = 490
        if serpiente[0].y >= 500:
            serpiente[0].y = 0
        elif serpiente[0].y < 0:
            serpiente[0].y = 490


if __name__ == '__main__':
    main()
    pygame.quit()
