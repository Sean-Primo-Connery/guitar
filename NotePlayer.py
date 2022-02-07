import random
import pygame


class note_player(object):
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, 2048)
        pygame.init()
        self.notes = {}

    def add(self, FileName):
        self.notes[FileName] = pygame.mixer.Sound(FileName)

    def play(self, FileName):
        try:
            self.notes[FileName].play()
        except:
            print(FileName + ' not found!')
