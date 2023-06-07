import lxml.etree as etree

# Avec ce script, on veut récupérer:
# PROBLÈME AVEC LES GLYPHES; ATTENTION.
# - le nombre total de graphèmes abrégés (suppose de partir de notre propre point de vue et de nos normes: dangereux?)
# - le nombre total de différents graphèmes visés
# - le nombre de graphèmes qui abrègent
# ATTENTION à bien exclure ce qui est de la pure normalisation.

def main():
    Z = "/home/mgl/Bureau/These/Edition/hyperregimiento-de-los-principes/Dedans/XML/analyse_linguistique/Sev_Z.xml"
    A = "/home/mgl/Bureau/These/Edition/hyperregimiento-de-los-principes/Dedans/XML/analyse_linguistique/Mad_A.xml"
    S = "/home/mgl/Bureau/These/Edition/hyperregimiento-de-los-principes/Dedans/XML/analyse_linguistique/Val_S.xml"
    input_xml = [Z, A, S]
    for xml_file in input_xml:
        print(xml_file.split("/")[-1].split("_")[-1].replace(".xml", ""))
        tei_namespace = 'http://www.tei-c.org/ns/1.0'
        NSMAP0 = {'tei': tei_namespace}
        with open(xml_file, "r") as input_file:
            parser = etree.XMLParser(load_dtd=True)
            f = etree.parse(input_file, parser=parser)
        root = f.getroot()
        all_att_n = root.xpath("//tei:choice[contains(@ana, '#normalisation')]/@n", namespaces=NSMAP0)
        different_att_n = list(set(all_att_n))
        different_att_n.sort()
        total_number_of_entities = len(all_att_n)
        print(total_number_of_entities)
        for entity in different_att_n:
            print(entity)
            number_of_occurrences = all_att_n.count(entity)
            print(number_of_occurrences)
        print("\n\n\n\n")

        # print(len(different_att_n))
        # print(f"Different entities: {[n for n in different_att_n]}")
        # different_orig_graphemes_no_glyphs = list(set(root.xpath("//tei:choice[contains(@ana, '#normalisation')]//node()[self::tei:abbr[not(tei:g)]|self::tei:orig[not(tei:g)]]/text()", namespaces=NSMAP0)))
        # glyphs = set(root.xpath("//tei:choice[contains(@ana, '#normalisation')]//node()[self::tei:abbr[tei:g]|self::tei:orig[tei:g]]/tei:g/@ref", namespaces=NSMAP0))
        # print(glyphs)
        # different_orig_graphemes_with_glyphs = [root.xpath(f"//tei:char[@xml:id = '{glyph.replace('#', '')}']/tei:mapping[1]/text()", namespaces=NSMAP0) for glyph in glyphs]
        # sum_orig_graphemes = different_orig_graphemes_no_glyphs + different_orig_graphemes_with_glyphs
        # print(len(sum_orig_graphemes))
        # exit(0)
        # different_norm_graphemes = set([text_node for text_node in root.xpath("//tei:choice[contains(@ana, '#normalisation')]//node()[self::tei:expan|self::tei:reg]/descendant-or-self::text()", namespaces=NSMAP0)])
        # print(different_orig_graphemes)
        # print(different_norm_graphemes)
        # exit(0)
    
        # homography_ratio = number_different_graphemes / number_orig_graphemes
        # print(f"Number of different graphemes: {number_different_graphemes}")
        # print(f"Total number of graphemes: {number_orig_graphemes}")
        # print(homography_ratio)

if __name__ == '__main__':
    main()