import os
import glob
import pandas as pd

os.chdir("./csv")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

if('completo.csv' in all_filenames):
    all_filenames.remove('completo.csv')

combined_csv = pd.concat([pd.read_csv(f, encoding='ANSI') for f in all_filenames ])
combined_csv.to_csv( "completo.csv", index=False, encoding='ANSI')