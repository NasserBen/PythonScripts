import os
import shutil

def organize_downloads():
    # Specify the path to the Downloads folder
    downloads_path = os.path.expanduser("~/Downloads")

    # Create a dictionary to map file extensions to folder names
    extension_mapping = {
        "txt": "TextFiles",
        "pdf": "PDFs",
        "jpg": "Images",
        "png": "Images",
        "zip": "ZipFiles",
        "mp4": "Videos"
        # Add more extensions and corresponding folder names as needed
    }

    # Create folders for each file type if they don't exist
    for folder_name in set(extension_mapping.values()):
        folder_path = os.path.join(downloads_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    # Get a list of all files in the Downloads folder
    files = [f for f in os.listdir(downloads_path) if os.path.isfile(os.path.join(downloads_path, f))]

    # Organize files based on their extensions
    for file in files:
        file_extension = file.split(".")[-1].lower()  # Get the file extension in lowercase
        destination_folder = extension_mapping.get(file_extension, "OtherFiles")

        source_path = os.path.join(downloads_path, file)
        destination_path = os.path.join(downloads_path, destination_folder, file)

        # Move the file to the appropriate folder
        shutil.move(source_path, destination_path)
        print(f"Moved {file} to {destination_folder} folder.")

if __name__ == "__main__":
    organize_downloads()
