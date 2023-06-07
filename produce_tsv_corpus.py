import lxml.etree as ET
import glob



with open('corpus.tsv', 'w') as output_file:
    output_file.truncate(0)
    
    
parser = ET.XMLParser(resolve_entities=False, dtd_validation=False,
                         load_dtd=True)  # inclure la DTD et résoudre les entités
tei = {'tei': 'http://www.tei-c.org/ns/1.0'}
corpus = glob.glob("/home/mgl/Bureau/These/Edition/collator/temoins_tokenises_regularises/*.xml")
for file in corpus:
    print(file)
    root = ET.parse(file)
    tokens = [''.join(word.xpath("descendant::text()")) for word in root.xpath("//tei:div[@type='partie'][@n='3']/descendant::tei:w", namespaces=tei)]
    lemmas = root.xpath("//tei:div[@type='partie'][@n='3']/descendant::tei:w/@lemma", namespaces=tei)
    pos = root.xpath("//tei:div[@type='partie'][@n='3']/descendant::tei:w/@pos", namespaces=tei)
    all_analysis = zip(tokens, lemmas, pos)
    # assert len(tokens) == len(lemmas) == len(pos)
    with open('corpus.tsv', 'a') as output_file:
        for token, lemma, pos in list(all_analysis):
            print(token.replace("\n", ""), lemma, pos)
            output_file.write(f"{token}\t{lemma}\t{pos}\n")