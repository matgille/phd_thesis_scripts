import sys
import re
import unicodedata
import glob

# Donné un caractère, sort les statistiques sur la position dans le mot.

def clean(input_file):
    space_regex = re.compile("\s+")
    input_file = re.sub(space_regex, " ", input_file)
    return input_file


def create_stats(input_file, char_to_study):
    basename_input_file = input_file.split("/")[-1].split(".")[0]
    with open(input_file, "r") as input_input_file:
        input_file = input_input_file.read()
    input_file = clean(input_file)
    input_file = unicodedata.normalize('NFD', input_file)
    with open(f".tmp/{basename_input_file}.log", "w") as input_log:
        input_log.write(input_file)
    indices = [i for i, x in enumerate(input_file) if x == char_to_study]

    stats_pos_initiale = 0
    stats_pos_finale = 0
    stats_pos_intermediaire = 0
    stats_avant_cesure = 0
    stats_avant_non_cesure = 0
    for index in indices:
        previous_char = input_file[index - 1]
        next_char = input_file[index + 1]

        if previous_char not in [' ', '-', '_'] and next_char not in [' ', '-', '_']:
            stats_pos_intermediaire += 1
        elif previous_char not in [' ', '-', '_'] and next_char == ' ':
            stats_pos_finale += 1
        elif previous_char == ' ' and next_char not in [' ', '-', '_']:
            stats_pos_initiale += 1
        elif previous_char not in [' ', '-', '_'] and next_char == '-':
            stats_avant_cesure += 1
        elif previous_char not in [' ', '-', '_'] and next_char == '_':
            stats_avant_non_cesure += 1



    with open(f"results/{basename_input_file}_{char_to_study}.tsv", "w") as output_input_file:
        output_input_file.write(f"Initiale: {stats_pos_initiale}\n"
                                f"Intermédiaire: {stats_pos_intermediaire}\n"
                                f"Finale: {stats_pos_finale}\n"
                                f"Avant césure par la ligne: {stats_avant_cesure}\n"
                                f"Avant non césure par la ligne: {stats_avant_non_cesure}")



# S'occuper de la normalisation parce que sinon ça va pas marcher.

if __name__ == '__main__':
    # On veut: la position intermédiaire; avant un espace; après un espace.
    files = ['/home/mgl/Bureau/These/Edition/hyperregimiento-de-los-principes/Statistiques/val_s_brut.txt',
             '/home/mgl/Bureau/These/Edition/hyperregimiento-de-los-principes/Statistiques/mad_a_brut.txt',
             '/home/mgl/Bureau/These/Edition/hyperregimiento-de-los-principes/Statistiques/sev_z_brut.txt',]
    chars = ['r', 's', 'ſ', 'ꝛ']
    for file in files:
        for char in chars:
            create_stats(file, char)
