# Unicode-Kannada-to-Shreelipi-Converter
This repository provides a tool to convert Kannada text from Unicode format to Shreelipi format. The project includes a script that processes all .txt files in a specified directory, converting each file to Shreelipi using a helper script (kannada-to-shreelipi.py). The converted files are saved in an Output directory inside the specified directory.

Prerequisites:

Python 3.x

Ensure the kannada-to-shreelipi.py script is available and functional. This helper script takes two arguments:

Input file path (the .txt file to be converted)
Output file path (where the converted file will be saved)

Cloning the Repository

To clone this repository, run:

git clone https://github.com/YathishPoojary98/Unicode-Kannada-to-Shreelipi-Converter.git

Then, navigate into the cloned directory:

cd Unicode-Kannada-to-Shreelipi-Converter

The script accepts one command-line argument:

Directory Path: The path to the directory containing .txt files to be processed.

Usage:

To run the script, use the following command:

python3 <script_name>.py <directory_path>

Example:

python3 convert_files.py /path/to/directory

How It Works:

Input Directory: The script scans the specified directory for .txt files.
Output Directory: The script creates an Output folder inside the given directory (if it doesn’t already exist).
File Processing: For each .txt file, the script invokes kannada-to-shreelipi.py and passes the input and output paths as arguments.
Error Handling: If any file fails to be processed, an error message will be printed for that specific file.

Example Output:

After running the script, the converted .txt files will be saved in the Output directory within the specified directory.
