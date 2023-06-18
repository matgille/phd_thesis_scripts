import sys




input_file = sys.argv[1]



with open(input_file, 'r') as input_file_csv:
    document = [line.replace('\n', '') for line in input_file_csv.readlines()]


with open("../data/corr.csv", "w") as output_file:
    for index, line in enumerate(document):
        elements = line.split(",")[1:]
        elements_cleaned = [value for value in elements if value != "NA"]
        print(elements_cleaned)
        if len(list(set(elements_cleaned))) == 2:
            interm_list = []
            for item in list(set(elements_cleaned)):
                interm_list.append(elements_cleaned.count(item))
            if 1 in interm_list:
                print("Variation unitaire, à supprimer")
            else:
                output_file.write(str(index) + "," + ",".join(elements) + "\n")
        else:
            output_file.write(str(index) + "," +",".join(elements) + "\n")
    
print("Data written to ../data/corr.csv")
exit()