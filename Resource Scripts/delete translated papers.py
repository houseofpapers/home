import os

def remove_specific_pdfs(folder_path):
    # Iterate through each folder and its contents
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.pdf'):
                file_path = os.path.join(root, file)
                # Check if the file contains any of the specified words
                if any(word in file.lower() for word in ['french', 'german', 'spanish']):
                    try:
                        # Attempt to remove the file
                        os.remove(file_path)
                        print(f"Removed: {file_path}")
                    except Exception as e:
                        print(f"Error removing {file_path}: {e}")

# Specify the parent folder path
parent_folder_path = r'C:\Users\veera\Desktop\Veer\Coding\Trial Website\pdfs\Economics_HL'

remove_specific_pdfs(parent_folder_path)
