from google.colab import drive
import pandas as pd
import requests

drive.mount('/content/drive')

tsv_file_path = '/content/drive/My Drive/path_to_your_file/dataset.tsv'
tsv_data = pd.read_csv(tsv_file_path, sep='\t')
print(tsv_data)

csv_file_path = '/content/drive/My Drive/path_to_your_file/dataset.csv'
csv_data = pd.read_csv(csv_file_path)
print(csv_data)

excel_file_path = '/content/drive/My Drive/path_to_your_file/dataset.xlsx'
excel_data = pd.read_excel(excel_file_path)
print(excel_data)

url = 'https://example.com/path_to_your_file.txt'
response = requests.get(url)

if response.status_code == 200:
    text_data = response.text
    print(text_data)
else:
    print("Failed to retrieve data from the URL")