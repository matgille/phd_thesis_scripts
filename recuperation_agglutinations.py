import glob
import re
import subprocess

for feature in ["agglutines", "deglutines"]:
    corpus = f"xsl/datasets/*_{feature}.txt"
    files = glob.glob(corpus)
    for file in files:
        basename = file.replace("xsl/datasets/", "").replace(f"_{feature}.txt", "")
        with open(file, "r") as input_file:
            file_as_string = input_file.read()
        print(file_as_string)
        patt = re.compile(r'[^\s]+X[^\s]+')
        strings = re.findall(pattern=patt, string=file_as_string)
        print(strings)
        strings.sort()
        to_lemmatize = "\n".join([element.replace("X", '\n') + "\n" for element in strings])
        list_of_agglutinations = "\n".join([element.replace("X", '') for element in strings])
        with open(f"xsl/datasets/{basename}_{feature}_only.txt", "w") as output_file:
            output_file.write(list_of_agglutinations)

        with open(f"xsl/datasets/{basename}_{feature}_only_to_lemmatize.tsv", "w") as output_file:
            output_file.write(to_lemmatize)

        cmd_sh = ["sh",
                  "/home/mgl/Bureau/These/Edition/collator/python/lemmatisation/analyze.sh",
                  f"xsl/datasets/{basename}_{feature}_only_to_lemmatize.txt",
                  f"xsl/datasets/{basename}_{feature}_only_lemmatized.txt"]
        subprocess.run(cmd_sh)