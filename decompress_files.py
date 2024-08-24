import os
import gzip
import shutil

# Path to the folder containing specified files
input_folder = '/home/bram/Documents/Strava data/export_26763577/activities'
output_folder = '/home/bram/Documents/Strava data/export_26763577/processed/gpx'

file_type = '.gpx.gz'

# Loop through all the files in the folder
for filename in os.listdir(input_folder):

    # Check if the file has the specified extension
    if filename.endswith(file_type):
        # Construct the full path to the file
        file_path = os.path.join(input_folder, filename)
        
        # Define the path for the decompressed file
        decompressed_file_path = os.path.join(output_folder, filename[:-3])  # Remove .gz

        # Decompress the .gz file
        with gzip.open(file_path, 'rb') as f_in:
            with open(decompressed_file_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        print(f'Decompressed: {filename} -> {os.path.basename(decompressed_file_path)}')

print('All files decompressed successfully.')