# Python File Organizer Script


### Decription
An easy-to-use Python script that helps you tidy up a directory by moving files into categorized subfolders based on their file extensions. This small utility was created as a final project for the CS50 Python course and is ideal for cleaning commonly cluttered directories (Downloads, Desktop, Pictures, etc.).

## Features
- Organizes files into folders by type (e.g., Images, Documents, Audio, Video, Archives).
- Supports a configurable set of known file extensions and categories.
- Safe moves only (no file content alteration).
- Interactive menu to select which standard folder to organize, or can be extended for custom folders.

## Why use this script?
If your downloads or desktop folder fills up with a mix of images, PDFs, installers, and other files, this script provides a quick way to sort items into sensible categories so you can find what you need faster and keep your system tidy.

## Supported categories and example extensions
The script groups files by common extensions. Typical categories include:
- **Images**: .jpg, .jpeg, .png, .gif, .bmp, .tiff
- **Documents**: .pdf, .docx, .doc, .txt, .odt
- **Spreadsheets**: .xls, .xlsx, .csv
- **Presentations**: .ppt, .pptx
- **Audio**: .mp3, .wav, .flac
- **Video**: .mp4, .mkv, .avi, .mov
- **Archives**: .zip, .tar, .gz, .rar

You can customize or extend mappings in the script to support other extensions if needed.

## How to run
1. Ensure you have Python 3.x installed.
2. From the project directory, run:

```powershell
python app.py
```

3. Follow the interactive menu to choose which folder (Pictures, Documents, Downloads, Desktop, Music, Videos, etc.) you'd like to organize, or extend the script to operate on any path.

> Note: This project previously referenced `project.py` — the correct entry point in this repository is `app.py`.

## Example usage
- Run the script and choose `Downloads` from the menu to move files into categorized subfolders within your Downloads folder.

## Safety & limitations
- This script moves files by extension only — it does not inspect file contents or metadata. If two files share the same name, you may need to handle naming conflicts (current behavior depends on implementation).
- Always run on a copy or test directory first if you are organizing important files.

## Extending the project
- Add a configuration file (YAML/JSON) to map categories to extensions dynamically.
- Add a dry-run mode so users can preview actions before files are moved.
- Add options to handle conflicts (rename, skip, or overwrite) and to operate recursively.

## Contributing & Credits
This project was created for the CS50 Python course. Contributions, improvements, and bug fixes are welcome — open a PR or issue with your suggestions.

---

Made with ❤️ for CS50
