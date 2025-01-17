import pygame
import sys
from button import Button
from slide import *


pygame.init()

SCREEN = pygame.display.set_mode((840, 680))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets\imgs\Background.png")
# set the pygame window name
pygame.display.set_caption('image')

# create a surface object, image is drawn on it.
imp = pygame.image.load("assets\imgs\slidelogo.png").convert()

# Using blit to copy content from one surface to other
SCREEN.blit(imp, (0, 0))
pygame.display.set_caption('Slide Puzzle Game')


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets\\fonts\\HKGrotesk-Regular.ttf", size)


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets\\fonts\\HKGrotesk-Regular.ttf", size)


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("::::: SLIDE :::::", True, "#29d250")
        MENU_RECT = MENU_TEXT.get_rect(center=(420, 100))
        PLAY_BUTTON = Button(image=pygame.image.load("assets\imgs\play_back.png"), pos=(420, 250),
                             text_input="PLAY", font=get_font(20), base_color="#000000", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets\imgs\opt_back.png"), pos=(420, 300),
                                text_input="OPTIONS", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets\imgs\quit_back.png"), pos=(420, 480),
                             text_input="QUIT", font=get_font(20), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    import options
                    options.main_menu_o()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
