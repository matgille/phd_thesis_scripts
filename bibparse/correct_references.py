import copy
# Adapté de https://bibtexparser.readthedocs.io/en/master/tutorial.html
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
import re
from lxml import etree

input_files = ["/home/mgl/Bureau/These/Edition/hyperregimiento-de-los-principes/Dedans/XML/corpus/biblio.bib",
               "/home/mgl/Bureau/These/Edition/hyperregimiento-de-los-principes/Dedans/XML/corpus/primary_sources.bib"]
input_these = "/home/mgl/Bureau/These/Edition/hyperregimiento-de-los-principes/Dedans/XML/corpus/corpus.xml"
input_edition = ""
chapitres = ['chevalerie', 'etat_recherche', 'relations', 'corpus', 'methodo', 'edition_electronique']
exclusion_list = ['primaire', 'primaire_edite', 'mss_omega', 'mss_B', 'autres_incunables', 'mss_B_incomplets', 'mss_A',
                  'lat', 'hors_corpus', 'bdd']


def get_references() -> {str: list}:
    """
    Cette fonction parse le XML de thèse et trie les références par chapitre.
    # TODO: gérer l'apparition multiple de références. Voir combien il y en a.
    :return: un dictionnaire de la forme {keyword: [refs]} où keyword sera le mot-clé du chapitre
    """
    tei = {'tei': 'http://www.tei-c.org/ns/1.0'}
    f = etree.parse(input_these)
    f.xinclude()
    root = f.getroot()
    references_by_chapter = {}
    chapters = root.xpath("//descendant::tei:TEI[@type='these']/descendant::tei:div[@type='chapitre']",
                          namespaces=tei)
    edition = root.xpath("//descendant::tei:TEI[@xml:id='castB' or @xml:id='castA' or @xml:id='lat' or @xml:id='hors_corpus']", namespaces=tei)
    for chapter in chapters:
        chapter_id = chapter.xpath("@xml:id")[0]
        if chapter_id in chapitres:
            list_of_refs = []
            refs = chapter.xpath("descendant::tei:ref[@type='biblio']/@target", namespaces=tei)
            for ref in refs:
                if " " in ref:
                    [list_of_refs.append(reference.replace('#', '')) for reference in ref.split()]
                else:
                    list_of_refs.append(ref.replace('#', ''))
            references_by_chapter[chapter_id] = list_of_refs

    refs = []
    for item in edition:
        refs.extend(reference for reference in item.xpath("descendant::tei:ref[@type='biblio']/@target", namespaces=tei))
    list_of_refs = []
    for ref in refs:
        if " " in ref:
            [list_of_refs.append(reference.replace('#', '')) for reference in ref.split()]
        else:
            list_of_refs.append(ref.replace('#', ''))
    references_by_chapter['edition_finale'] = list_of_refs
    return references_by_chapter

def replacement(match):
    print(match)
    return match.group(1).lower()

def clean_dates(string):
    string = string.replace("{", "").replace("}", "")
    if "siècles" in string:
        print(string)
    pattern1 = re.compile(r'([xviXVI])e?-([xviXVI])e [Ss]i[èe]cles?')
    pattern2 = re.compile(r'([xviXVI]+)e?-([xviXVI]+)e [Ss]i[èe]cles?')
    if re.findall(pattern2, string):
        print("It's a match!")
        print(string)
        string = re.sub(pattern2, replacement, string)
        print(string)
    return string


def biblio_per_chapter():
    refs = get_references()
    parser = BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    parser.homogenise_fields = False
    parser.interpolate_strings = True

    bibliography = ""
    for bib_file in input_files:
        with open(bib_file) as biblatex_file:
            bibliography += "\n"
            bibliography += biblatex_file.read()
    bib_database = bibtexparser.loads(bibliography, parser)
    bib_database = bib_database.entries
    output_keys = [entry['ID'] for entry in bib_database]

    # On va vérifier si la base de sortie est identique à celle d'entrée
    # (Bibtexparser ne dit pas si une entrée est mal formée)
    pattern = re.compile(r'\n@[^\n]*')
    input_keys = [first_line.split("{")[1].replace(',', '') for first_line in re.findall(pattern, bibliography)]
    difference = list(set(input_keys) - set(output_keys))
    if len(difference) > 0:
        print("Un problème a été trouvé avec une (ou plus) de vos références. Veuillez vérifier:")
        print(difference)




    annotated_refs = []
    entrytypes = []
    for ref in bib_database:
        entrytypes.append(ref['ENTRYTYPE'])
        try:
            ref['title']
        except KeyError:
            try:
                if ref['keywords'] not in ['primaire', 'mss_A', "mss_B_incomplets", ""]:
                    print("No title")
                    print(ref)
            except KeyError as e:
                print("No title")
                print(ref)
        if ref['ENTRYTYPE'] not in ['online', 'unpublished', 'software', 'video', 'report', 'document']:
            try:
                ref.pop('urldate')
            except KeyError:
                pass
            try:
                # Let's remove the day in the dates.
                date = ref['date']
                if len(date.split('-')) > 2:
                    date = '-'.join(date.split('-')[:2])
                ref['date'] = date
            except KeyError as e:
                pass
        try:
            if ref['keywords'] in exclusion_list:
                annotated_refs.append(ref)
                if ref['ENTRYTYPE'] == 'phdthesis':
                    try:
                        ref['institution']
                    except KeyError as e:
                        print(f"Missing institution in phdthesis {ref['ID']}")
                continue
        except KeyError:
            pass
        try:
            annotation = [keyword for keyword, references in refs.items() if ref['ID'] in references][0]
        except IndexError:
            annotation = ''
        try:
            # On veut le premier chapitre d'apparition, sauf si le mot clé est spécifié dans la bdd bibliographique (dans ce cas on le garde)
            if ref['keywords'] in chapitres:
                pass
            else:
                ref['keywords'] = annotation
        except KeyError:
            if annotation != '':
                ref['keywords'] = annotation
                # On va vérifier les entrées pour les thèses.
                if ref['ENTRYTYPE'] == 'phdthesis':
                    try:
                        ref['institution']
                    except KeyError as e:
                        print(f"Missing institution in phdthesis {ref['ID']}")
                elif ref['ENTRYTYPE'] in ['book', 'incollection', 'inproceedings']:
                    try:
                        ref['location']
                    except KeyError as e:
                        pass
                    try:
                        ref['isbn']
                    except KeyError as e:
                        try:
                            ref['doi']
                        except KeyError:
                            print(f"Missing isbn in book {ref['ID']}")
                            if ref['ENTRYTYPE'] == 'book':
                                print(ref["title"])
                            elif ref['ENTRYTYPE'] in ['incollection', 'inproceedings']:
                                print(ref["booktitle"])

        annotated_refs.append(ref)


    db = BibDatabase()
    db.entries = annotated_refs
    writer = BibTexWriter()
    with open('/home/mgl/Bureau/These/Edition/hyperregimiento-de-los-principes/Dedans/XML/corpus/annotated_refs.bib',
              'w') as bibfile:
        bibfile.write(writer.write(db))



if __name__ == '__main__':
    biblio_per_chapter()
