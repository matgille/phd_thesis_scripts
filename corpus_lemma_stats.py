import lxml.etree as ET



corpus = "/home/mgl/Bureau/These/Edition/collator/temoins_tokenises_regularises/Mad_G.xml"
parser = ET.XMLParser(resolve_entities=False, dtd_validation=False,
                         load_dtd=True)  # inclure la DTD et résoudre les entités
tei = {'tei': 'http://www.tei-c.org/ns/1.0'}
root = ET.parse(corpus)
root.xinclude()

tokens = root.xpath("//tei:w/text()", namespaces=tei)
lemmas = root.xpath("//tei:w/@lemma", namespaces=tei)

length_corpus = len(tokens)
different_forms = len(set(tokens))
different_lemmas = len(set(lemmas))

print(f"Corpus size: {length_corpus}\n"
      f"Unique forms: {different_forms}\n"
      f"Unique lemmas: {different_lemmas}")

