import os

def rename_pdfs(parent_folder):
    # Iterate through each folder in the parent folder
    for folder_name in os.listdir(parent_folder):
        folder_path = os.path.join(parent_folder, folder_name)

        # Check if the item in the parent folder is a directory
        if os.path.isdir(folder_path):
            # Get the first two words of the folder name
            first_two_words = ' '.join(folder_name.split()[:2])

            # Iterate through PDF files in the current folder
            for filename in os.listdir(folder_path):
                if filename.endswith('.pdf'):
                    old_filepath = os.path.join(folder_path, filename)

                    # Construct the new filename
                    new_filename = f"{first_two_words}_{filename}"

                    new_filepath = os.path.join(folder_path, new_filename)

                    # Rename the file
                    os.rename(old_filepath, new_filepath)
                    print(f"Renamed: {filename} to {new_filename}")

# Replace 'C:\\Users\\veera\\Desktop\\Veer\\Coding\\Trial Website\\pdfs\\Spanish_B_SL' 
# with the actual path to your parent folder
parent_folder_path = r'C:\Users\veera\Desktop\Veer\Coding\Trial Website\pdfs\Spanish_B_SL'
rename_pdfs(parent_folder_path)
