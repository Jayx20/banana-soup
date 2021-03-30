import pygame


class Sprite:
    img: pygame.Surface
    rect: pygame.Rect

    def __init__(self, img_path: str):
        self.img = pygame.image.load('assets/'+img_path)  # load the image from name
        self.rect = pygame.Rect((0, 0), self.img.get_size())  # use the whole image
        self.img.convert()  # renders loaded image for later drawing

