from bs4 import BeautifulSoup
import pandas
import os
import glob

from utils import remove_duplicates, process

os.chdir("./xls")

extension = 'xls'
file_names = [i for i in glob.glob('*.{}'.format(extension))]

for file_name in file_names:
    f = open(file_name, 'r', encoding='ANSI')

    soup = BeautifulSoup(f, 'html.parser')
    overview = soup.find('table', attrs={'rules':'all'})
    rows = overview.find_all('tr')

    content = []

    for row in rows:
        row_content = []
        elements = row.find_all('td')
        for i in range(len(elements)):
            element = elements[i]
            raw = element.text.strip()
            
            clean = clean(raw, i)

            row_content.append(clean)
        
        if not all('' == s or s.isspace() for s in row_content):
            content.append(row_content)     

    headers = content.pop(0)

    remove_duplicates(content)

    df = pandas.DataFrame(content, columns=headers)

    os.chdir("../csv")
    df.to_csv(file_name.split('.')[0] + '.csv', index=False, encoding='ANSI')
    os.chdir("../xls")