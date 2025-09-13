import pandas as pd
import os

data = {'Name':['Alice' , 'Bob' , 'Charlie'],
        'Age': [25 , 27 , 29],
        'City': ['Africa' , 'Banglore','Chicago']}

df = pd.DataFrame(data)

#Ensure the "data" directory exists at the root level

data_dir = "data"
os.makedirs(data_dir , exist_ok=True)

#Define the file path
file_path = os.path.join(data_dir , 'sample_data.csv')

#save the df to a csv file , including column names
df.to_csv(file_path , index=False)

print(f"csv file saved to {file_path}")