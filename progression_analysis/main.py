import glob
import sys
from lxml import etree
import re
import matplotlib.pyplot as plt
import numpy as np

# Script qui permet de donner la progression d'un lemme ou d'une expression sur l'ensemble du corpus dans
# le texte.


corpus_path = glob.glob("/home/mgl/Bureau/These/Edition/collator/temoins_tokenises_regularises/*.xml")


def run_query(query: tuple, group_by: str, file: str, dodge_value:float) -> tuple:
    frequency_and_position = [(1, 0)]
    div_dict = {}
    tei_ns = 'http://www.tei-c.org/ns/1.0'
    ns_decl = {'tei': tei_ns}
    expression, element_to_match = query
    with open(file, "r") as input_file:
        print(file)
        difference_list = []
        root = etree.parse(input_file)
        position = 0
        number_of_words = 0
        if element_to_match == "word":
            expression = re.compile(expression)
            for indice, group in enumerate(root.xpath(group_by, namespaces=ns_decl)):
                div_n = int(group.xpath("self::tei:div[@type='chapitre']/@n | ancestor::tei:div[@type='chapitre']/@n", namespaces=ns_decl)[0])
                words_per_div = 0
                div_dict[div_n] = 100 * div_n
                words = group.xpath("descendant::tei:w", namespaces=ns_decl)
                position += 100
                for index, word in enumerate(words):
                    relative_position = (index/len(words))*100
                    if isinstance(word.text, str) and re.match(expression, word.text):
                        number_of_words += 1
                        words_per_div += 1
                        frequency_and_position.append((position + relative_position, number_of_words + dodge_value))
                    if index == len(words) - 1:
                        difference_list.append((div_n+dodge_value, words_per_div))
                        frequency_and_position.append((position + relative_position, number_of_words+ dodge_value))
        elif element_to_match == "lemma":
            for div_n, group in enumerate(root.xpath(group_by, namespaces=ns_decl)):
                words_per_div = 0
                div_n = int(group.xpath("self::tei:div[@type='chapitre']/@n | ancestor::tei:div[@type='chapitre']/@n", namespaces=ns_decl)[0])
                div_dict[div_n] = 100 * div_n
                words = group.xpath(f"descendant::tei:w", namespaces=ns_decl)
                position += 100
                for index, word in enumerate(words):
                    relative_position = (index / len(words)) * 100
                    if word.xpath(f"@lemma='{expression}'"):
                        number_of_words += 1
                        words_per_div += 1
                        frequency_and_position.append((position + relative_position, number_of_words + dodge_value))
                    if index == len(words) - 1:
                        difference_list.append((div_n+dodge_value, words_per_div))
                        frequency_and_position.append((position + relative_position, number_of_words + dodge_value))
        elif element_to_match == "pos":
            for group in root.xpath(group_by, namespaces=ns_decl):
                pass
        return frequency_and_position, div_dict, file.split("/")[-1].split(".xml")[0], query, difference_list


def main(query: tuple, group_by, plot_title):
    result_list = []
    dodge_value = 0
    for xml_file in corpus_path:
        dodge_value += 0.02
        result_list.append(run_query(query, group_by, xml_file, dodge_value))
    plot_result(result_list, group_by, plot_title)

def plot_result(list_of_results, group_by, plot_title):
    fig, (progression, evolution) = plt.subplots(2, figsize=(15,10))
    for index, (frequency, divs, witness, query, difference_list) in enumerate(list_of_results):
        expression, element = query
        if len(frequency) != 0:
            progression_result = [list(element) for element in list(zip(*frequency))]
            evolution_result = [list(element) for element in list(zip(*difference_list))]
            progression.plot(progression_result[0], progression_result[1], label=witness)
            plt.xticks(range(1, len(divs) + 1))
            [progression.axvline(x = value, color = 'g', ls='dashed') for key, value in divs.items()]
            [progression.text(value, 0, key) for key, value in divs.items()]
            evolution.plot(evolution_result[0], evolution_result[1], 'o', label=witness)
            plt.xticks(range(1, len(divs) + 1))
            plt.grid(axis = 'y')
    plt.legend(title=f'Couleur des témoins:')
    if element == 'word':
        element = 'forme'
    else:
        pass
    fig.suptitle(f"Requête ({element}): {expression}. Requête {group_by}")
    progression.set_title(f'Progression par témoin. L\'axe des abscisses correspond au pourcentage de mots cumulé par chapitre')
    evolution.set_title(f"Nombre d'occurrences par chapitre et par témoin")
    print(plot_title)
    plt.savefig(f'images/{expression.replace("*", "-ast-")}_{element}{plot_title}.png', dpi=300)
    plt.show()


if __name__ == '__main__':
    expression = sys.argv[1]
    element_to_match = sys.argv[2]
    expression_and_element = (expression, element_to_match)
    group_by = sys.argv[3]
    if len(sys.argv) == 5:
        plot_additional_title = "_" + sys.argv[4]
    else:
        plot_additional_title = ""
    print(expression_and_element, group_by)
    main(expression_and_element, group_by, plot_additional_title)
