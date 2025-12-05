import os,shutil

downloads = "/Users/kalaivani/Downloads"

folders = {
"Images" : [".jpg",".png",".jpeg",".gif",".bmp"],
"Docs" : [".pdf",".docx",".doc",".txt",".xlsx",".pptx"],
"ZIP" : [".zip",".rar",".7z"],
}

for file in os.listdir(downloads):
    filename,ext = os.path.splitext(file)
    print ("file name"+filename)
    print ("Ext"+ext)
    for folder,ext_list in folders.items():
        if ext in ext_list:
            os.makedirs(os.path.join(downloads, folder), exist_ok=True)
            shutil.move(os.path.join(downloads, file), os.path.join(downloads, folder, file))
print("-------------------")
            
