# Stefano Di Michelangelo
# 20221110024

correo = [input("crea un correo electronico con por lo menos una mayuscula, un @ y su direccion \n Crea un correo: ")]
tipodecorreo = []
corre = []
#no me acorde el nombre de la funcion 
listaletras = ["Q","W","E","R","T","Y",'U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
listaslice = ["Q","W","E","R","T","Y",'U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','@','gmail','hotmail','yahoo','.','.com','.org',".edu"]
    
#no me acorde el nombre de la funcion 

correo2 = correo.slice(listaslice)

if "@" in correo2:

        if "gmail" or "hotmail" or "yahoo":
            tipodecorreo = ("personal")

        if ".com" or ".org" in correo2:
            print ("Tu correo personal", correo, "es valido")
        elif ".edu": 
            tipodecorreo = ("educativo")
            print ("Tu correo educativo", correo, "es valido")
        else:
            print("Tu correo no es valido por falta de parametros")
else:
   print("Tu correo no es valido por falta de parametros")
