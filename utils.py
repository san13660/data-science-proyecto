from unidecode import unidecode

def clean(string, column=0):
    processed = " ".join(string.split())
    processed = processed.replace('"','')
    processed = processed.replace("'","")
    processed = processed.replace('À','Á')
    processed = processed.replace('È','É')
    processed = processed.replace('Ì','Í')
    processed = processed.replace('Ò','Ó')
    processed = processed.replace('Ù','Ú')

    processed = processed.replace('CION','CIÓN')
    processed = processed.replace('LINGUE','LINGÜE')
    processed = processed.replace('%','Ñ')

    if(column not in [0,1,5]):
        processed = processed.replace('-','')

    return processed

def remove_duplicates(content):
    to_check = [3,4]
    to_pop = []
    for i in range(len(content) - 1):
        for j in range(i+1, len(content)):
            duplicate = True
            for column in to_check:
                if(unidecode(content[i][column]) != unidecode(content[j][column])):
                    duplicate = False
                    break
            if(duplicate):
                value_i = content[i][4].count('Á') + content[i][4].count('É') + content[i][4].count('Í') + content[i][4].count('Ó') + content[i][4].count('Ú') + content[i][4].count('Ü')
                value_j = content[j][4].count('Á') + content[j][4].count('É') + content[j][4].count('Í') + content[j][4].count('Ó') + content[j][4].count('Ú') + content[j][4].count('Ü')

                if(value_j > value_i):
                    if(i not in to_pop):
                        to_pop.append(i)
                else:
                    if(j not in to_pop):
                        to_pop.append(j)
    
    to_pop.sort(reverse=True)

    for index in to_pop:
        content.pop(index)