import os

def list_pdf_files(folder_path):
    pdf_files = []
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith('.pdf'):
            pdf_files.append(file_name)
    return pdf_files

# Replace 'your/desktop/folder/path' with the path to your desktop folder
desktop_folder_path = r'C:\Users\Rishi Mody\Documents\GitHub\Trial-Website\pdfs\French_B_SL\2018 May Examination Session'
pdf_files = list_pdf_files(desktop_folder_path)
print(pdf_files)

div_str = '''<div class="paper-year">
<p><strong>2021 May</strong></p>
'''
# Print the names of PDF files
for i in range(len(pdf_files)):
    div_str += ''' <p class="paper-title"><a href="PATH" target="_blank">DESCRIPTOR</a></p>'''
    div_str+="\n"
    div_str = div_str.replace("PATH", "pdfs/French_B_SL/2018 May Examination Session/" + pdf_files[i])
    
div_str+='''</div>'''
print("\n")
print(div_str)
DESCRIPTOR = ""


split_paths = div_str.split("\n")
new_paths=[]

for path in split_paths:
    DESCRIPTOR = ""
    print(path)
    if "paper_1__SL_markscheme" in path:
      DESCRIPTOR = "Paper 1 SL Markscheme"
      path = path.replace("DESCRIPTOR", DESCRIPTOR)
      new_paths.append(path)
    elif "paper_1__SL" in path:
      DESCRIPTOR = "Paper 1 SL"
      path = path.replace("DESCRIPTOR", DESCRIPTOR)
      new_paths.append(path)
    elif "paper_2_reading_comprehension__question_booklet_SL" in path:
      DESCRIPTOR = "Paper 2 SL Question Booklet"
      path = path.replace("DESCRIPTOR", DESCRIPTOR)
      new_paths.append(path)
    elif "paper_2_reading_comprehension__text_booklet_SL" in path:
      DESCRIPTOR = "Paper 2 SL Text Booklet"
      path = path.replace("DESCRIPTOR", DESCRIPTOR)
      new_paths.append(path)
    elif "paper_2_reading_comprehension__SL_markscheme" in path:
      DESCRIPTOR = "Paper 2 SL Markscheme"   
      path = path.replace("DESCRIPTOR", DESCRIPTOR)
      new_paths.append(path)
    elif "listening_comprehension__SL" in path:
      DESCRIPTOR = "Listening Comprehension SL"
      path = path.replace("DESCRIPTOR", DESCRIPTOR)
      new_paths.append(path)
    elif "listening_comprehension__SL_markscheme" in path:
      DESCRIPTOR = "Listening Comprehension SL Markscheme"
      path = path.replace("DESCRIPTOR", DESCRIPTOR)
      new_paths.append(path)
    elif "paper_1__question_booklet_SL" in path:
      DESCRIPTOR = "Paper 1 SL Question Booklet"
      path = path.replace("DESCRIPTOR", DESCRIPTOR)
      new_paths.append(path)
    elif "paper_1__text_booklet_SL" in path:
      DESCRIPTOR = "Paper 1 SL Text Booklet"
      path = path.replace("DESCRIPTOR", DESCRIPTOR)
      new_paths.append(path)
    elif "paper_2__SL" in path:
      DESCRIPTOR = "Paper 2 SL"
      path = path.replace("DESCRIPTOR", DESCRIPTOR)
      new_paths.append(path)
    elif "paper_2__SL_markscheme" in path:
      DESCRIPTOR = "Paper 2 SL Markscheme"
      path = path.replace("DESCRIPTOR", DESCRIPTOR)
      new_paths.append(path)
      
      
    print(DESCRIPTOR)
print("\n")
end_str = '''<div class="paper-year">
  <p><strong>2018 May</strong></p> '''
end_str += '\n'.join(new_paths)
end_str += '''</div>'''
print(end_str)
