import os
import shutil
from pathlib import Path

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

def organize_desktop():
    desktop_path = Path.home() / "Desktop"
    
    if not desktop_path.exists():
        print("Desktop folder not found!")
        return
    
    for folder in FILE_CATEGORIES.keys():
        folder_path = desktop_path / folder
        folder_path.mkdir(exist_ok=True)
    
    for item in desktop_path.iterdir():
        if item.is_file():
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if item.suffix.lower() in extensions:
                    shutil.move(str(item), str(desktop_path / category / item.name))
                    moved = True
                    break
            
            if not moved:
                shutil.move(str(item), str(desktop_path / "Others" / item.name))
    
    print("Files organized successfully!")

if __name__ == "__main__":
    organize_desktop()
