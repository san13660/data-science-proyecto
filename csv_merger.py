import os
import glob
import pandas as pd

os.chdir("./csv")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

if('todos_departamentos.csv' in all_filenames):
    all_filenames.remove('todos_departamentos.csv')

combined_csv = pd.concat([pd.read_csv(f, dtype=object, encoding='ANSI') for f in all_filenames ])
combined_csv.to_csv( "todos_departamentos.csv", index=False, encoding='ANSI')