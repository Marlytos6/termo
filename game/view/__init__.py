import pygame
from pygame import draw
from pygame import rect

font = pygame.font.get_default_font()

def text(display:pygame.surface.Surface, text, size, x, y):
    global font
    fonte = pygame.font.Font(font, size)
    text_surface = fonte.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    display.blit(text_surface, text_rect)
def palavra(display:pygame.surface.Surface, x, y, w, h):
    x -= w / 2
    draw.rect(display, (0, 255, 0), rect.Rect(x, y, w, h))
