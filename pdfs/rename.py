import os

def rename_pdfs(folder_path):
    # Get the first two words of the folder name
    first_two_words = ' '.join(os.path.basename(folder_path).split()[:2])

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

# Replace 'C:\\Users\\veera\\Desktop\\Veer\\Coding\\Trial Website\\pdfs\\2021 November Examination Session' 
# with the actual path to your folder
folder_path = r'C:\Users\veera\Desktop\Veer\Coding\Trial Website\pdfs\2021 November Examination Session'
rename_pdfs(folder_path)
