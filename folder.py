import os, shutil
os.mkdir('C:\\Pramod\\file handle/.txt')
os.mkdir('C:\\Pramod\\file handle/.jpg')
os.mkdir('C:\\Pramod\\file handle/.xml')
list_files=os.listdir('C:\\Pramod\\open cv')
for folder in list:
    if folder == '.jpg':
       list.delete(folder)
    elif folder =='.txt':
        list.delete(folder)
    elif folder =='.xml':
        list.delete(folder) 
for file in list_files:
   if file.endswith(".jpg"):
      src_dir="C:\\Pramod\\open cv/"
      dst_dir="C:\\Pramod\\file handle\\.jpg" 
      shutil.move(src_dir,dst_dir)  
   elif file.endswith(".txt"):
        src_dir="C:\Pramod\Anaconda\\files"
        dst_dir="C:\\Pramod\\file handle\\.txt" 
        shutil.move(src_dir,dst_dir) 
   elif file.endswith(".xml"):
        src_dir="C:\Pramod\Anaconda\\files"
        dst_dir="C:\\Pramod\\file handle\\.xml" 
        shutil.move(src_dir,dst_dir) 

 