import os

def delete_files_with_keywords(folder_path, keywords):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            for keyword in keywords:
                if keyword.lower() in file.lower():
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")

# Replace with the actual path to your main folder
folder_path = r'C:\Users\veera\Desktop\Chemistry_HL'

# Specify the keywords to check for in the file names
keywords_to_check = ['spanish', 'french','Spanish','French','German','german']

delete_files_with_keywords(folder_path, keywords_to_check)
