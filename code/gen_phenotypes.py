import os
import shutil
import pandas as pd
import csv


# Read in sublist-all.txt and generate a list of sub-##### to be used for file filtering
def read_usable_subs(filename):
    with open(filename, 'r') as file:
        usable_subs = [line.strip() for line in file]
    return usable_subs


# Eliminate any sub-##### that aren't specified in sublist-all.txt
def eliminate_subs(filename, usable_subs):
    with open(filename, 'r') as file:
        lines = file.readlines()

    header = lines[0]  
    data_lines = lines[1:]  

    filtered_data_lines = [line for line in data_lines if any(line.strip().startswith(id) for id in usable_subs)]

    with open(filename, 'w') as file:
        file.write(header)  
        file.writelines(filtered_data_lines)


# Format the first column for BIDS specification
# This function applies "participant_id to the first cell for every measure and applies sub- to the beginning of every ID"
def format_first_column(filename):
    with open(filename, 'r') as infile:
        reader = csv.reader(infile)
        rows = list(reader)

    if rows:
        for row in rows[1:]:
            if row and len(row) > 0:
                row[0] = f'sub-{row[0]}'

    with open(filename, 'w', newline='') as infile:
        writer = csv.writer(infile)
        writer.writerows(rows)

    with open(filename, 'r') as infile:
                lines = infile.readlines()

    if lines:
        header = lines[0]
        header = header.replace(header.split('\t')[0], "participant_id")

    with open(filename, 'w') as infile:
        infile.write(header)
        infile.writelines(lines[1:])


# Iterate through the .tsv that were generated to eliminate unwanted subs and apply BIDS formatting
def process_files(folder_path, usable_subs):
    for filename in os.listdir(folder_path):
        if filename.endswith('.tsv'):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, 'r') as infile:
                reader = csv.reader(infile)
                rows = list(reader)

            with open(file_path, 'w', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerows(rows)

            eliminate_subs(file_path, usable_subs)
            format_first_column(file_path)

            print(f"Processed: {file_path}")


# File converts all .txt files that exist in /sourcedata/redcap for processing defined above
def convert_to_tsv(input_path, output_path):
    for filename in os.listdir(input_path):
        if filename.endswith('.txt'):
            txt_file_path = os.path.join(input_path, filename)
            if filename == "participants.txt":
                tsv_file_path = os.path.join(bids_directory, filename.replace('.txt', '.tsv'))
            else:
                tsv_file_path = os.path.join(output_path, filename.replace('.txt', '.tsv'))

            df = pd.read_csv(txt_file_path, sep='\t', na_values=["n/a"])
            df.to_csv(tsv_file_path, sep='\t', index=False, na_rep="n/a")

            print(f"Converted: {txt_file_path} to {tsv_file_path}")

# Specify paths and call functions
if __name__ == "__main__":
    # Relative path to the usable_subs file
    code_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(code_directory)
    bids_directory = os.path.join(parent_directory, 'bids')
    usable_subs = read_usable_subs(os.path.join(code_directory, 'sublist-all.txt'))

    # Relative path to the input and output directories
    # if statement will delete overwrite existing files if you need to run script again
    input_path = os.path.join(parent_directory, 'bids/sourcedata/redcap/')
    output_path = os.path.join(parent_directory, 'bids/phenotype/')
    
    # Check if output path exists and only delete non-.json files
    if os.path.exists(output_path):
        for filename in os.listdir(output_path):
            if not filename.endswith('.json'):
                file_path = os.path.join(output_path, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)

    # Recreate the directory or create a new one
    os.makedirs(output_path, exist_ok=True)

    # Run functions to convert and process files
    convert_to_tsv(input_path, output_path)
    process_files(output_path, usable_subs)
    process_files(bids_directory, usable_subs)
