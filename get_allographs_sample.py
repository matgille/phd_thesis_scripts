import os
import random
import shutil
import sys

def get_only_dir(path):
    all_docs = os.listdir(path)
    only_dirs = [element for element in all_docs if '.png' not in element]
    only_dirs.sort()
    return only_dirs


samples = int(sys.argv[1])
paths = ['/home/mgl/Bureau/These/Edition/scripts/retrieve_graphemes/img/val_s/graphemes', '/home/mgl/Bureau/These/Edition/scripts/retrieve_graphemes/img/mss_15304/graphemes']
path_out = '/home/mgl/Bureau/These/Edition/hyperregimiento-de-los-principes/Dedans/Facsimiles/images_these/allographs'
dict = {0: 'S', 1: 'A'}
for index, path in enumerate(paths):
    with open(f'includegraphics_{dict[index]}.txt', 'w') as txt_file:
        txt_file.truncate(0)
    with open(f'includegraphics_{dict[index]}.txt', 'a') as txt_file:
        allographs = get_only_dir(path)
        for allograph in allographs:
            print(allograph)
            txt_file.write(f"\nAllograph: {allograph}\n\n")
            txt_file.write(r"<figure>")
            try:
                os.mkdir(f"{path_out}/{allograph}")
            except FileExistsError:
                pass
            try:
                os.mkdir(f"{path_out}/{allograph}/{dict[index]}")
            except FileExistsError:
                pass

            # get list of images
            images = os.listdir(f"{path}/{allograph}")
            random.shuffle(images)
            sample = images[:samples]
            print(sample)
            for image in sample:
                txt_file.write(f'<graphic scale="1" url=\"{path_out}/{allograph}/{dict[index]}/{image}\"/>\n')
                shutil.copy(f"{path}/{allograph}/{image}", f"{path_out}/{allograph}/{dict[index]}/{image}")

            txt_file.write(f'<desc>Réalisations du {allograph} dans {dict[index]}.</desc>')
            txt_file.write("</figure>")
