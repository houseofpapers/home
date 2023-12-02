import os
sessions = ["2014 May", "2014 November", "2015 May", "2015 November", "2016 May", "2016 November", "2017 May", "2017 November", "2018 May", "2018 November", "2019 May", "2019 November", "2020 November","2021 May", "2021 November", "2022 May", "2022 November", "2023 May"]
#reverse order of sessions in above list
sessions.reverse()

def list_pdf_files(folder_path):
      pdf_files = []
      for file_name in os.listdir(folder_path):
          if file_name.lower().endswith('.pdf'):
              pdf_files.append(file_name)
      return pdf_files
for session in sessions:
  # Replace 'your/desktop/folder/path' with the path to your desktop folder
  desktop_folder_path = r'C:\Users\Rishi Mody\Documents\GitHub\Trial-Website\pdfs\Economics_SL' + '\\' + session + ' Examination Session'
  
  pdf_files = list_pdf_files(desktop_folder_path)
  

  div_str = ""
  # Print the names of PDF files
  for i in range(len(pdf_files)):
      div_str += ''' <p class="paper-title"><a href="PATH" target="_blank">DESCRIPTOR</a></p>'''
      div_str+="\n"
      div_str = div_str.replace("PATH", "pdfs/Economics_SL" + '/' + session + " Examination Session/" + pdf_files[i])
      


  DESCRIPTOR = ""


  split_paths = div_str.split("\n")
  new_paths=[]

  for path in split_paths:
      DESCRIPTOR = ""
      
      if "Spanish" in path:
        path = ""
      elif "French" in path:
        path = ""
      elif "paper_1_SLSL_markscheme" in path or "paper_1__SLSL_markscheme" in path:
        DESCRIPTOR = "Paper 1 SL/SL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1_SLSL" in path or "paper_1__SLSL" in path:
        DESCRIPTOR = "Paper 1 SL/SL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_2_SLSL_markscheme" in path or "paper_2__SLSL_markscheme" in path:
        DESCRIPTOR = "Paper 2 SL/SL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_2_SLSL" in path or "paper_2__SLSL" in path:
        DESCRIPTOR = "Paper 2 SL/SL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1_TZ1_SLSL_markscheme" in path or "paper_1__TZ1_SLSL_markscheme" in path:
        DESCRIPTOR = "Paper 1 TZ1 SL/SL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1_TZ1_SLSL" in path or "paper_1__TZ1_SLSL" in path:
        DESCRIPTOR = "Paper 1 TZ1 SL/SL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1_TZ1_SL_markscheme" in path or "paper_1__TZ1_SL_markscheme" in path:
        DESCRIPTOR = "Paper 1 TZ1 SL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1_TZ1_SL" in path or "paper_1__TZ1_SL" in path:
        DESCRIPTOR = "Paper 1 TZ1 SL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1_TZ2_SL_markscheme" in path or "paper_1__TZ2_SL_markscheme" in path:
        DESCRIPTOR = "Paper 1 TZ2 SL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1_TZ2_SL" in path or "paper_1__TZ2_SL" in path:
        DESCRIPTOR = "Paper 1 TZ2 SL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1__SL_markscheme" in path or "paper_1_SL_markscheme" in path:
        DESCRIPTOR = "Paper 1 SL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1__SL" in path or "paper_1_SL" in path:
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
      elif "listening_comprehension__SL_markscheme" in path:
        DESCRIPTOR = "Listening Comprehension SL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "listening_comprehension__SL" in path:
        DESCRIPTOR = "Listening Comprehension SL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1_question_booklet_SL" in path:
        DESCRIPTOR = "Paper 1 SL Question Booklet"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1_text_booklet_SL" in path:
        DESCRIPTOR = "Paper 1 SL Text Booklet"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_2_SL_markscheme" in path or "paper_2__SL_markscheme" in path:
        DESCRIPTOR = "Paper 2 SL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_2_SL" in path or "paper_2__SL" in path:
        DESCRIPTOR = "Paper 2 SL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_3_SL_markscheme" in path or "paper_3__SL_markscheme" in path:
        DESCRIPTOR = "Paper 3 SL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_3_SL" in path or "paper_3__SL" in path:
        DESCRIPTOR = "Paper 3 SL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_2_TZ1_SL_markscheme" in path or "paper_2__TZ1_SL_markscheme" in path:
        DESCRIPTOR = "Paper 2 TZ1 SL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_2_TZ1_SL" in path or "paper_2__TZ1_SL" in path:
        DESCRIPTOR = "Paper 2 TZ1 SL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_2_TZ2_SL_markscheme" in path or "paper_2__TZ2_SL_markscheme" in path:
        DESCRIPTOR = "Paper 2 TZ2 SL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_2_TZ2_SL" in path or "paper_2__TZ2_SL" in path:
        DESCRIPTOR = "Paper 2 TZ2 SL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_3_TZ1_SL_markscheme" in path or "paper_3__TZ1_SL_markscheme" in path:
        DESCRIPTOR = "Paper 3 TZ1 SL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_3_TZ1_SL" in path or "paper_3__TZ1_SL" in path:
        DESCRIPTOR = "Paper 3 TZ1 SL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_3_TZ2_SL_markscheme" in path or "paper_3__TZ2_SL_markscheme" in path:
        DESCRIPTOR = "Paper 3 TZ2 SL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_3_TZ2_SL" in path or "paper_3__TZ2_SL" in path:
        DESCRIPTOR = "Paper 3 TZ2 SL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      
        
        
      
  
  end_str = r'<div class="paper-year"> <p><strong>' + session + r'</strong></p>'
  end_str += '\n'.join(new_paths)
  end_str += '''</div>'''
  print(end_str)
  print("\n")
