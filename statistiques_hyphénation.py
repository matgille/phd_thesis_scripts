import numpy as np


with open('sev_z_brut.txt', 'r') as input_text_file:
    text = input_text_file.readlines()

print(np.mean([len(line) for line in text if '⸗' in line and '-' in line]))
print(np.mean([len(line) for line in text if '⸗' not in line and '-' in line]))