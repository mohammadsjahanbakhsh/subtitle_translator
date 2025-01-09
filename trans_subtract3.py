from multiprocessing import Pool 
#! pip install googletrans==3.1.0a0
from googletrans import Translator
from os import listdir  , cpu_count
from tqdm.auto import tqdm
from time import time 

translator = Translator()
path_split = lambda path : path.rsplit(".",maxsplit=1)[0]+'.'

def has_str(string):
  for s in string:
    if s.isalpha():
      return True
  return False
def file_translator(sub):
    sub = str(sub)
    if len(sub)<4:  return sub
    elif sub.strip().isnumeric(): return sub
    elif ":" in sub: return sub
    elif sub[0].isalpha(): return  "\n".join([translator.translate(sub.strip(), dest='fa').text  ,sub]   )
    elif has_str(sub): return  "\n".join([translator.translate(sub.strip(), dest='fa').text  ,sub ]  )
    return sub
def read_text(path):
  with open(path,'r') as f:
    return f.readlines()
def write_text(list_text,path):
  with open(path,'w') as f:
    f.write("".join(list_text))
def read_trans_write(file_path,format_out):
  #try:
    t1= time()
    with Pool(cpu_count() -1) as p:    
        old_sub = list(read_text(file_path))
        new_sub = list(tqdm(p.imap(file_translator , old_sub) , total = len(old_sub),desc=file_path.rsplit("\\")[-1]))
        #new_sub = p.map(file_translator , old_sub)
        #new_sub.append("@mohammads_j")
        path_without_format  = path_split(file_path)
        print(path_without_format +format_out)
        write_text(new_sub , path_without_format + format_out)   
  #except:print("somting wrong :")
  #else: print("Successful:",round((time()-t1)/60 , 3) ," --> ",path_without_format.rsplit("\\",maxsplit=1)[-1][:-1])
def translate_multi_file():
  path = input("enter path of folder:")
  format_in= input("format input(without dot):")
  format_out = input("format output(without dot):")
  try:    files  = [x for x in listdir(path) if x.endswith(format_in)]
  except:    print("problem in path or format")
  else:  
    
    for file in tqdm(files,desc=path.rsplit("\\",maxsplit=1)[-1]):
        #print(file)
        
        read_trans_write(path+"\\"+file,format_out)   
if __name__ == '__main__':
    while True:
        mul_one = input("1 multi files &OR& 2 one file ?:")
        if "1" in mul_one or "2" in mul_one:break  
    if "1" in mul_one :
        translate_multi_file()
    elif "2" in mul_one:
        path_file = input("path of file :")
        format_out = input("enter format output :")
        read_trans_write(path_file,format_out)

