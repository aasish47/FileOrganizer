import os
import shutil
def organize_files(folder_path):
    # it gives the different forlders different names
    # Iterate through all files in the folder
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            # Split the file name and extension
            _, extension = os.path.splitext(file_name)
            extension = extension[1:]  # Remove the dot from the extension

            # Create a folder with the extension name if it doesn't exist
            if not os.path.exists(os.path.join(folder_path, extension)):
                os.makedirs(os.path.join(folder_path, extension))

            # Move the file to the respective folder
            src = os.path.join(folder_path, file_name)
            dest = os.path.join(folder_path, extension, file_name)
            shutil.move(src, dest)

def organize_files(folder_path):
    # Define custom names for folders based on extensions
    folder_names = {
        '.txt': 'Text Files',
        '.doc': 'Word Documents',
        '.jpg': 'JPEG Images',
        '.mp3': 'MP3 Music',
        '.py': 'Python Scripts',
        'ppm': 'Presentations',
        # Add more extensions and folder names as needed
    }

    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            _, extension = os.path.splitext(file_name)
            extension = extension.lower()

            if extension in folder_names:
                folder_name = folder_names[extension]
            else:
                folder_name = 'Other Files'

            # Create the folder if it doesn't exist
            folder_path_new = os.path.join(folder_path, folder_name)
            if not os.path.exists(folder_path_new):
                os.makedirs(folder_path_new)

            # Move the file to the respective folder
            src = os.path.join(folder_path, file_name)
            dest = os.path.join(folder_path_new, file_name)
            shutil.move(src, dest)

folder_path = "D:\ZZZZZZ"
organize_files(folder_path)

