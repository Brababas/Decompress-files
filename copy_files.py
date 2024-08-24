import os
import shutil

# Path to the folder containing files
input_folder = '/home/bram/Documents/Strava data/export_26763577/activities'
output_folder = '/home/bram/Documents/Strava data/export_26763577/processed/fit'

file_type = '.fit'

# Loop through all the files in the folder
for filename in os.listdir(input_folder):

    # Check if the file has the specified extension
    if filename.endswith(file_type):
        # Construct the full path to the file
        file_path = os.path.join(input_folder, filename)
        
        # Define the path for the copied file
        output_file_path = os.path.join(output_folder, filename)

        # Decompress the .gz file
        with open(file_path, 'rb') as f_in:
            with open(output_file_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        print(f'Copied: {filename} -> {os.path.basename(output_file_path)}')

print('All files copied successfully.')