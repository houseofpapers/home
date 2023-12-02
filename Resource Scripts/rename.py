import os

def rename_pdfs(parent_folder):
    for folder_name in os.listdir(parent_folder):
        folder_path = os.path.join(parent_folder, folder_name)

        if os.path.isdir(folder_path):
            first_two_words = ' '.join(folder_name.split()[:2])

            for filename in os.listdir(folder_path):
                if filename.endswith('.pdf'):
                    old_filepath = os.path.join(folder_path, filename)

                    new_filename = f"{first_two_words}_{filename}"

                    new_filepath = os.path.join(folder_path, new_filename)

                    os.rename(old_filepath, new_filepath)
                    print(f"Renamed: {filename} to {new_filename}")

parent_folder_path = r'C:\Users\veera\Desktop\psych'
rename_pdfs(parent_folder_path)
