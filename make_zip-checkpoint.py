import zipfile
import os
import sys

# Define the name of the final zip file
zip_filename = 'CVProject_RockPaperScissors.zip'

# List all files and directories to include in the zip
files_to_zip = [
    'Rock–Paper–Scissors.ipynb',  # Your report/analysis
    'main.py',                    # GUI launcher
    'tkinter_interface.py',       # GUI code
    'game_logic.py',              # Core logic/AI (Ensure this matches your file name!)
    'simulate.py',                # Simulation code
    'make_zip.py'                 # Include the zipper script itself
]

def create_zip_archive():
    """Creates a zip file containing all project files."""
    print(f"Creating {zip_filename}...")
    
    try:
        # Create a ZipFile object in write mode
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files_to_zip:
                if os.path.exists(file):
                    # Add the file to the zip archive
                    zipf.write(file)
                    print(f"  Added {file}")
                else:
                    print(f"  Warning: File not found - {file}")

        print("\nZip archive creation complete!")
        print(f"File saved as: {os.path.abspath(zip_filename)}")

    except Exception as e:
        print(f"\nAn error occurred during zipping: {e}")
        sys.exit(1)

if __name__ == '__main__':
    create_zip_archive()