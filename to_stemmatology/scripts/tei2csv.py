from lxml import etree
import glob


tei_ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
xmlFile = "/home/mgl/Bureau/These/Edition/collator/results/Sev_Z.xml"
xml_input = etree.parse(xmlFile)
xml_input.xinclude()
sigla = ["Mad_A", "Mad_B", "Mad_G", "Sal_J", "Esc_Q", "Sev_R", "Sev_Z", "Phil_U"]
all_apps = xml_input.xpath("//tei:app", namespaces=tei_ns)

with open("../data/output_full.csv", "w") as output_file:
    output_file.write(",".join(siglum for siglum in sigla) + "\n")
    for index_apps, apparatus in enumerate(all_apps):
        interm_dict = {}
        for index_rdgGrp, rdgGrp in enumerate(apparatus.xpath("descendant::tei:rdgGrp", namespaces=tei_ns)):
            wits = " ".join(rdgGrp.xpath("descendant::tei:rdg/@wit", namespaces=tei_ns)).split()
            if len(rdgGrp.xpath("descendant::tei:w", namespaces=tei_ns)) > 0:
                interm_line = {wit.replace('#', ""): index_rdgGrp + 1 for wit in wits}
            else:
                interm_line = {wit.replace('#', ""): 0 for wit in wits}
            interm_dict.update(interm_line)

        # On ajoute les omissions
        for siglum in sigla:
            try:
                interm_dict[siglum]
            except KeyError:
                interm_dict[siglum] = 0



        line = [str(interm_dict[siglum]) for siglum in sigla]
        output_file.write(",".join(line) + "\n")




