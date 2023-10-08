# -*- coding: utf-8 -*-
from multiprocessing import Pool 
#! pip install googletrans==3.1.0a0
from googletrans import Translator
from os import listdir  , cpu_count
from tqdm.auto import tqdm
from time import time 

translator = Translator()

def path_split(path):
  path_name = path.rsplit(".",maxsplit=1)[0]+'.'

  return path_name


def has_str(string):
  for s in string:
    if s.isalpha():
      return True
  return False


def file_translator(sub):
    sub = str(sub)
    if len (sub)<3:
        return sub
    elif sub.strip().isnumeric():
        #print(sub) #############################################
        return sub
    elif ":" in sub:
        return sub
    
    elif sub[0].isalpha():
        return  translator.translate(sub.strip(), dest='fa').text +"\n"
    elif has_str(sub):
        return  translator.translate(sub.strip(), dest='fa').text +'\n'
        
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
        new_sub = list(tqdm(p.imap(file_translator , old_sub) , total = len(old_sub)))
        #new_sub = p.map(file_translator , old_sub)
        new_sub.append("@mohammads_j")
    path_without_format  = path_split(file_path)
    print(path_without_format +format_out)
    write_text(new_sub , path_without_format + format_out)
    
  #except:print("somting wrong :")
    
  #else:

    print("Successful:",round((time()-t1)/60 , 3) ," --> ",path_without_format.rsplit("\\",maxsplit=1)[-1][:-1])

    # new_sub=file_translator(read_text(file))
    # folder_path  = path_split(file)
    # write_text(new_sub,folder_path+'.'+format_out)

# path_name = "/content/1-1 How to use dates & times with pandas - Python.vtt"
if __name__ == '__main__':

    path_file = input("path of file :")

    format_out = input("enter format output :")

    read_trans_write(path_file,format_out)

