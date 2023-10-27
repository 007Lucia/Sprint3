import os 

class Inicializar():
    basedir = os.path.abspath(os.path.join(__file__,"../../"))
    DateFormat = "%d/%m/%Y"     
    HourFormat =  "%H%M%S"      
    
    Json = basedir + "/Pages"
    Environment = "Dev"
    NAVEGADOR = "Edge"
    Path_evidencias = basedir + "/data/evidencia"
    
    if Environment == "Dev":
        URL = "https://shop.thonet-vander.com/" 
        User = ""
        Password = ""       