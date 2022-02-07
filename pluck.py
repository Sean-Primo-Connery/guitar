import sys
import pygame
import NotePlayer
import tune_pre
import chord

if __name__ == "__main__":

    n = NotePlayer.note_player()
    tune_matrix = tune_pre.tune_pre(n)
    chord_dir = chord.chord()

    key_list = [pygame.K_RSUPER, pygame.K_RALT, pygame.K_p, pygame.K_LEFTBRACKET, pygame.K_RIGHTBRACKET,
                pygame.K_BACKSLASH]
    case_list = [
        f"guitar/{tune_matrix['6chord'][0]}.wav",
        f"guitar/{tune_matrix['5chord'][0]}.wav",
        f"guitar/{tune_matrix['4chord'][0]}.wav",
        f"guitar/{tune_matrix['3chord'][0]}.wav",
        f"guitar/{tune_matrix['2chord'][0]}.wav",
        f"guitar/{tune_matrix['1chord'][0]}.wav",
    ]

    if len(key_list) != len(case_list):
        raise Exception("key_list not match case_list")
    else:
        pygame.init()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key in list(chord_dir.keys()):
                        case_list = [
                            f"guitar/{tune_matrix['6chord'][int(chord_dir[event.key][0])]}.wav",
                            f"guitar/{tune_matrix['5chord'][int(chord_dir[event.key][1])]}.wav",
                            f"guitar/{tune_matrix['4chord'][int(chord_dir[event.key][2])]}.wav",
                            f"guitar/{tune_matrix['3chord'][int(chord_dir[event.key][3])]}.wav",
                            f"guitar/{tune_matrix['2chord'][int(chord_dir[event.key][4])]}.wav",
                            f"guitar/{tune_matrix['1chord'][int(chord_dir[event.key][5])]}.wav",
                        ]
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    elif event.key in key_list:
                        n.play(case_list[key_list.index(event.key)])
