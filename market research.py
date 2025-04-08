import zipfile
import os
# Define the file path
zip_file_path = "/mnt/data/archive.zip"
extract_folder = "/mnt/data/india_healthcare_data"
# Extract the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
zip_ref.extractall(extract_folder)
# List the extracted files
extracted_files = os.listdir(extract_folder)
extracted_files


import pandas as pd
# Load a few key datasets to inspect their structure
file_samples = [
"allo-doc-PHCS_2017.csv",
"facilities-PHCS_2017.csv",
"functioning-PHCS_2017.csv",
"rural-population-centre_2017.csv",
"worker-female-subcen_2017.csv"
]
# Read the first few rows of each file
sample_data = {file: pd.read_csv(os.path.join(extract_folder, file)).head() for file in
file_samples}
