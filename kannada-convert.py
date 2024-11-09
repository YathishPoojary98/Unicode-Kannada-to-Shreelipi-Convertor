import os
import sys
import subprocess

# Define the directory containing the files
directory = sys.argv[1]

# Define the output directory
output_dir = f"{sys.argv[1]}/Output"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate through each file in the directory
for filename in os.listdir(directory):
    # Create the full path to the file
    file_path = os.path.join(directory, filename)

    # Check if it's a regular file and ends with .txt
    if os.path.isfile(file_path) and filename.endswith('.txt'):
        # Prepare the output file path
        output_path = os.path.join(output_dir, filename)
        
        # Prepare the command to run the other Python script
        command = ['python3', 'kannada-to-shreelipi.py', file_path, output_path]
        
        # Execute the command
        try:
            subprocess.run(command, check=True)
            print(f"Processed {file_path} successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error processing {file_path}: {e}")
