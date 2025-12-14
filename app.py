# With love 💖 for CS50

import shutil
from pathlib import Path
import time
import sys

# Define the folders and their corresponding file extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Programs": [".exe", ".msi", ".bat", ".sh"],
    "Others": []  # Default folder for unknown file types
}

OPTIONS = ['Pictures', 'Documents', 'Downloads', 'Desktop', 'Music', 'Videos', 'Exit']
CHOICES = ('1', '2', '3', '4', '5', '6', '7')

# Display user options
def display_options():
    print("\nWelcome To FIle Organizer.\n")
    for count, folder in enumerate(OPTIONS, start=1):
        print(f"{count}. {folder}")

# Get user choices
def get_choice():
    display_options()
    while True:
        try:
            choice = input("Select the directory you want to organize: ")
            if choice not in CHOICES:
                print("Invalid choice. Try again.")
                continue
            return choice
        except ValueError:
            print("Invalid choice. Try again.")
            continue

# Print success messages 
def message():
    print("Processing...")
    time.sleep(3)
    print("Files organized successfully!\n")

# Handle file organisation logic
def organize_files(dir):
    path = Path.home() / dir

    if not path.exists():
        print(f"{dir} folder not found!\n")
        return
    
    for folder in FILE_CATEGORIES.keys():
        folder_path = path / folder
        folder_path.mkdir(exist_ok=True)
    
    for item in path.iterdir():
        if item.is_file():
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if item.suffix.lower() in extensions:
                    shutil.move(str(item), str(path / category / item.name))
                    moved = True
                    break
            
            if not moved:
                shutil.move(str(item), str(path / "Others" / item.name))
    message()

def main():
    
    choice = get_choice()

    if choice == '1':
        organize_files("Pictures")
    elif choice == '2':
        organize_files("Documents")
    elif choice == '3':
        organize_files("Downloads")
    elif choice == '4':
        organize_files("Desktop")
    elif choice == '5':
        organize_files("Music")
    elif choice == '6':
        organize_files("Videos")
    elif choice == '7':
        print("Exiting...")
        time.sleep(2)
        sys.exit()

if __name__ == "__main__":
    main()
