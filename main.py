import pygame
import os

pygame.init()

directory = os.getcwd()
bg = pygame.image.load(f'{directory}/images/backround.jpeg')

music = f'{directory}\Music\Смешарики - От винта!.mp3'
pygame.mixer.music.load(music)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
sound1 = pygame.mixer.Sound(f'{directory}\Music\Звук взрыва.mp3')
sound1.set_volume(0.3)
set_mus = True


def draw(screen):
    font = pygame.font.Font(None, 50)
    text = font.render("Game over!", True, (255, 0, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))


class Plane:
    def __init__(self):
        super().__init__()
        self.img1 = pygame.image.load(f'{directory}\images\plane1_1.png')
        self.img1 = pygame.transform.scale(self.img1, (50, 35))
        self.img1_rot1 = pygame.transform.rotate(self.img1, 45)
        self.img1_rot2 = pygame.transform.rotate(self.img1, -45)
        self.boom = pygame.image.load(f'{directory}\images\Взрыв.png')
        self.boom = pygame.transform.scale(self.boom, (100, 70))
        self.x, self.y = 100, 200
        self.v = 2

    def move(self):
        self.v = -self.v
        return self.x, self.y, self.v

    def update_plane(self):
        global set_mus
        if self.y + 35 > height:
            screen.blit(bg, (0, 0))
            screen.blit(self.boom, (self.x, self.y - 20))
            pygame.mixer.music.stop()
            draw(screen)
            if set_mus:
                sound1.play()
                set_mus = False
        else:
            self.y += self.v
            if self.y < 0:
                self.v = -self.v
            self.y += self.v
            screen.blit(bg, (0, 0))
            self.img1 = self.transform_plane()
            screen.blit(self.img1, (self.x, self.y))

    def delta_v(self):
        self.v = -self.v

    def transform_plane(self):
        if self.v < 0:
            return self.img1_rot1
        else:
            return self.img1_rot2


if __name__ == '__main__':
    pygame.display.set_caption('Вроде игра, хотя на мусор больше похоже')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    clock = pygame.time.Clock()
    player = Plane()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.delta_v()
        player.update_plane()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
