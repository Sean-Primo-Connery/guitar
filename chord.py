import pandas as pd
import pygame


def chord():
    chord_list = [
        pygame.K_q,
        pygame.K_e,
        pygame.K_d,
        pygame.K_c,
        pygame.K_g,
        pygame.K_a,
        pygame.K_f,
        pygame.K_r,
        pygame.K_v,
        pygame.K_w,
    ]
    chords = pd.read_excel('chord.xlsx')
    dic = {}
    for i in range(len(chord_list)):
        lis = []
        for cho in list(chords.columns):
            lis.append(chords.loc[i, cho])
        dic[chord_list[i]] = lis

    return dic
