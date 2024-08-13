import os 
import PyInstaller
import tkinter
from tkinter.filedialog import askdirectory

caminho = askdirectory(title='Selecione uma pasta ')

lista_arquivos = os.listdir(caminho)

locais = {
        "imagens": [".png",".jpg",".gif",".webp"],
        "planilhas": [".xlsx"],
    "documentos" : [".pdf",".docx",".ppt",".pbix","txt"],
    "csv": [".csv"],
    "video":[".mp4",".wmv",".avi",".mov",],
    "atalho": [".lnk"],
    "programas":[".exe"],
    "compactados" :[".zip",".rar"],
    "Torrent" : [".torrent"]
    
}   

for arquivo in lista_arquivos: 
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
    

tkinter.messagebox.showinfo(title=None, message="concluído", options= None)
           
            

            
         
            

