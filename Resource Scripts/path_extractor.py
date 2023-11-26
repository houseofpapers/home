import os
sessions = ["2000 November", "2001 May", "2001 November", "2002 May", "2002 November", "2003 May", "2003 November", "2004 May", "2004 November", "2005 May", "2005 November", "2006 May", "2006 November", "2007 May", "2007 November", "2008 November", "2009 November", "2010 May", "2010 November", "2011 May", "2011 November", "2012 May", "2012 November", "2013 May", "2013 November", "2014 May", "2014 November", "2015 May", "2015 November", "2016 May", "2016 November", "2017 May", "2017 November", "2018 May", "2018 November", "2019 May", "2019 November", "2020 November", "2021 May", "2021 November", "2022 May", "2022 November"]
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
  desktop_folder_path = r'C:\Users\Rishi Mody\Documents\GitHub\Trial-Website\pdfs\Psychology_HL' + '\\' + session + ' Examination Session'
  
  pdf_files = list_pdf_files(desktop_folder_path)
  

  div_str = ""
  # Print the names of PDF files
  for i in range(len(pdf_files)):
      div_str += ''' <p class="paper-title"><a href="PATH" target="_blank">DESCRIPTOR</a></p>'''
      div_str+="\n"
      div_str = div_str.replace("PATH", "pdfs/Psychology_HL" + '/' + session + " Examination Session/" + pdf_files[i])
      


  DESCRIPTOR = ""


  split_paths = div_str.split("\n")
  new_paths=[]

  for path in split_paths:
      DESCRIPTOR = ""
      
      if "Spanish" in path:
        path = ""
      elif "French" in path:
        path = ""
      elif "paper_1_HLSL_markscheme" in path or "paper_1__HLSL_markscheme" in path:
        DESCRIPTOR = "Paper 1 HL/SL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1_HLSL" in path or "paper_1__HLSL" in path:
        DESCRIPTOR = "Paper 1 HL/SL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_2_HLSL_markscheme" in path or "paper_2__HLSL_markscheme" in path:
        DESCRIPTOR = "Paper 2 HL/SL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_2_HLSL" in path or "paper_2__HLSL" in path:
        DESCRIPTOR = "Paper 2 HL/SL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1_TZ1_HLSL_markscheme" in path or "paper_1__TZ1_HLSL_markscheme" in path:
        DESCRIPTOR = "Paper 1 TZ1 HL/SL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1_TZ1_HLSL" in path or "paper_1__TZ1_HLSL" in path:
        DESCRIPTOR = "Paper 1 TZ1 HL/SL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1_TZ1_HL_markscheme" in path or "paper_1__TZ1_HL_markscheme" in path:
        DESCRIPTOR = "Paper 1 TZ1 HL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1_TZ1_HL" in path or "paper_1__TZ1_HL" in path:
        DESCRIPTOR = "Paper 1 TZ1 HL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1_TZ2_HL_markscheme" in path or "paper_1__TZ2_HL_markscheme" in path:
        DESCRIPTOR = "Paper 1 TZ2 HL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1_TZ2_HL" in path or "paper_1__TZ2_HL" in path:
        DESCRIPTOR = "Paper 1 TZ2 HL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1__HL_markscheme" in path or "paper_1_HL_markscheme" in path:
        DESCRIPTOR = "Paper 1 HL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1__HL" in path or "paper_1_HL" in path:
        DESCRIPTOR = "Paper 1 HL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_2_reading_comprehension__question_booklet_HL" in path:
        DESCRIPTOR = "Paper 2 HL Question Booklet"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_2_reading_comprehension__text_booklet_HL" in path:
        DESCRIPTOR = "Paper 2 HL Text Booklet"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_2_reading_comprehension__HL_markscheme" in path:
        DESCRIPTOR = "Paper 2 HL Markscheme"   
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "listening_comprehension__HL_markscheme" in path:
        DESCRIPTOR = "Listening Comprehension HL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "listening_comprehension__HL" in path:
        DESCRIPTOR = "Listening Comprehension HL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1_question_booklet_HL" in path:
        DESCRIPTOR = "Paper 1 HL Question Booklet"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_1_text_booklet_HL" in path:
        DESCRIPTOR = "Paper 1 HL Text Booklet"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_2_HL_markscheme" in path or "paper_2__HL_markscheme" in path:
        DESCRIPTOR = "Paper 2 HL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_2_HL" in path or "paper_2__HL" in path:
        DESCRIPTOR = "Paper 2 HL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_3_HL_markscheme" in path or "paper_3__HL_markscheme" in path:
        DESCRIPTOR = "Paper 3 HL Markscheme"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
      elif "paper_3_HL" in path or "paper_3__HL" in path:
        DESCRIPTOR = "Paper 3 HL"
        path = path.replace("DESCRIPTOR", DESCRIPTOR)
        new_paths.append(path)
        
        
      
  
  end_str = r'<div class="paper-year"> <p><strong>' + session + r'</strong></p>'
  end_str += '\n'.join(new_paths)
  end_str += '''</div>'''
  print(end_str)
  print("\n")
