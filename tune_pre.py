import pandas as pd
import write_wave


def tune_pre(n_pygame):
    tune = pd.read_excel('guitar_tune.xlsx', index_col='pin')
    tune_matrix = {}
    for chord in tune.columns:
        tune_matrix.setdefault(chord, [])
        for pin in tune.index:
            write_wave.WriteWave('guitar', tune.loc[pin, chord])
            n_pygame.add(f'guitar/{tune.loc[pin, chord]}.wav')
            tune_matrix[chord].append(tune.loc[pin, chord])

    return tune_matrix
