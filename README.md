# 📝 Unicode-Kannada-to-Shreelipi Converter

This repository provides a tool to **convert Kannada text from Unicode format to Shreelipi format**. The script processes all `.txt` files in a specified directory, converting each file using a helper script (`kannada-to-shreelipi.py`). The converted files are saved in an **Output** directory within the specified directory.

---

## 🚀 Prerequisites

- **Python 3.x**
- Ensure the `kannada-to-shreelipi.py` script is available and functional.

### **Helper Script (`kannada-to-shreelipi.py`):**
- **Input:** Path to the `.txt` file containing Unicode Kannada text.
- **Output:** Path where the converted Shreelipi text will be saved.

---

## 📥 Cloning the Repository

To clone this repository, run:

```bash
git clone https://github.com/YathishPoojary98/Unicode-Kannada-to-Shreelipi-Converter.git
```
Then, navigate into the cloned directory:


```bash
cd Unicode-Kannada-to-Shreelipi-Converter
```
📌 Usage
The script accepts one command-line argument:

Directory Path – The path to the directory containing .txt files to be processed.
To run the script, use the following command:

```bash
python3 <script_name>.py <directory_path>
```
Example
```bash
python3 convert_files.py /path/to/directory
```
🔍 How It Works
1️⃣ Input Directory: The script scans the specified directory for .txt files.
2️⃣ Output Directory: An Output folder is created inside the given directory (if it doesn’t already exist).
3️⃣ File Processing: Each .txt file is passed to kannada-to-shreelipi.py for conversion.
4️⃣ Error Handling: If a file fails to be processed, an error message is printed for that specific file.

📂 Example Output
After running the script, the converted .txt files will be saved in the Output directory within the specified directory.

