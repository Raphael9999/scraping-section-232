import os
import glob
import pandas as pd

work_dir = os.getcwd()
os.chdir("result/")
all_filenames = [i for i in glob.glob(f'extract232*.csv')]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

# sort
combined_csv.sort_values('Request ID', inplace = True)

# remove duplicates
combined_csv.drop_duplicates(subset='Request ID', keep = 'last', inplace = True) 

# enforce type
# combined_csv['Request ID'] = combined_csv['Request ID'].astype('int32', errors='ignore')
combined_csv['Request ID'] = pd.to_numeric(combined_csv['Request ID'], downcast='integer', errors='coerce')
combined_csv.dropna(subset=['Request ID'], inplace=True)
combined_csv['Request ID'] = combined_csv['Request ID'].astype('int32', errors='ignore')

# print list of missing
lower = int(combined_csv.iloc[0, 0])
higher = int(combined_csv.iloc[-1, 0]+1)
rg = pd.Series(range(lower, higher))
missing = rg[~rg.isin(combined_csv['Request ID'])].tolist()
print(f'Missing Request ID: {missing}')

# export to csv
combined_filename = f"extract232_{lower}-{higher}.csv"
combined_csv.to_csv(combined_filename, index=False, encoding='utf-8')

# delete merged files
all_filenames = [ f for f in all_filenames if f != combined_filename] # remove new file...
for f in all_filenames:
    os.remove(f)

os.chdir(work_dir)