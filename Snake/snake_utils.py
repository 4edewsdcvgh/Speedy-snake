import pygame
import sys
from play import play
from pygame import mixer

#making music
mixer.init()
mixer.music.load("Assets/Music/Party's Cancelled.ogg")
mixer.music.play()


pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
background = pygame.image.load("Assets/snake_graphics/Graphics/background.png")

def get_font(size):
    return pygame.font.Font("Assets/Fonts/robot-9000-font/Robot9000-MVxZx.ttf", size)

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image if image else font.render(text_input, True, base_color)
        self.rect = self.image.get_rect(center=pos)
        self.text_input = text_input
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color

    def update(self, screen):
        screen.blit(self.image, self.rect)

    def check_for_input(self, position):
        return self.rect.collidepoint(position)

    def change_color(self, position):
        if self.rect.collidepoint(position):
            self.image = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.image = self.font.render(self.text_input, True, self.base_color)

def main_menu():
    while True:
        screen.blit(background, (0, 0))
        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("SPEEDY SNAKE", True, "#964B00")
        menu_rect = menu_text.get_rect(center=(640, 100))
        screen.blit(menu_text, menu_rect)

        play_button = Button(image=pygame.image.load("Assets/Play Rect.png"), pos=(740, 250),
                             text_input="PLAY", font=get_font(75), base_color="#964B00", hovering_color="White")

        quit_button = Button(image=pygame.image.load("Assets/Quit Rect.png"), pos=(740, 350),
                             text_input="QUIT", font=get_font(75), base_color="#964B00", hovering_color="White")

        for button in [play_button, quit_button]:
            button.change_color(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_input(menu_mouse_pos):
                    play()
                if quit_button.check_for_input(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()