import pandas as pd

with open("/path/tsv_file.tsv") as tsv_file:
    data = []

    for line in tsv_file:
        data.append(line.split("\t"))   

df = pd.DataFrame(data)
new_header = df.iloc[0]
df = df[1:]
df.columns = new_header

df.to_csv('/path/new_csv_file_name.csv')
