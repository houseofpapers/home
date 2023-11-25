import os
from PyPDF2 import PdfReader
import re

def extract_text_from_pages(pdf_file, start_page, end_page):
    with open(pdf_file, 'rb') as file:
        pdf_reader = PdfReader(file)
        num_pages = len(pdf_reader.pages)

        # Ensure end_page is within the valid range
        end_page = min(end_page, num_pages)

        text = ''
        for page_num in range(start_page - 1, end_page):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def clean_text(text):
    # Remove non-alphabetic characters and split into words
    words = re.findall(r'\b[A-Za-z]+\b', text)
    return ' '.join(words)

def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".pdf") and "markscheme" in filename.lower():
                file_path = os.path.join(root, filename)

                # Extract text from pages 4 and 5
                text_from_page_4 = extract_text_from_pages(file_path, 4, 5)
                text_from_page_5 = extract_text_from_pages(file_path, 5, 6)

                # Check if the pages are within the valid range
                if text_from_page_4 or text_from_page_5:
                    # Clean the text
                    cleaned_text_4 = clean_text(text_from_page_4)
                    cleaned_text_5 = clean_text(text_from_page_5)

                    # Get the first 20 words
                    first_20_words_4 = cleaned_text_4.split()[:20]
                    first_20_words_5 = cleaned_text_5.split()[:20]

                    # Check if any specified words are present
                    specified_words = {
                        'article': 'Article',
                        'comic': 'Comic',
                        'infographic': 'Infographic',
                        'advertisement': 'Advertisement',
                        'blog': 'Blog',
                        'cartoon': 'Cartoon',
                        'opinion': 'Opinion',
                    }

                    found_types = []

                    for word in first_20_words_4:
                        if word.lower() in specified_words:
                            found_types.append(specified_words[word.lower()])

                    for word in first_20_words_5:
                        if word.lower() in specified_words:
                            found_types.append(specified_words[word.lower()])

                    if found_types:
                        print(f"File: {file_path}\nFound Types: {', '.join(found_types)}\n")
                    else:
                        print(f"File: {file_path}\nNOT IN PAGE RANGE\n")
                        
def main(main_folder_path):
    process_folder(main_folder_path)

if __name__ == "__main__":
    main_folder_path = r"C:\Users\veera\Desktop\algo"
    main(main_folder_path)
