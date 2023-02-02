# Stefano Di Michelangelo
# 20221110024

miau_edd = [
        {
            "name": "Pelusa",
            "gender": "Male",
            "age": 9,
            "weight": 3.5,
            "colour": "Blanco",
            "vaccinated": False
        },
        {
            "name": "Oreo",
            "gender": "Male",
            "age": 1,
            "weight": 3.7,
            "colour": "Blanco y Negro",
            "vaccinated": False
        },
        {
            "name": "Bebeso",
            "gender": "Female",
            "age": 10,
            "weight": 4.1,
            "colour": "Blanco",
            "vaccinated": False
        },
        {
            "name": "Lilly",
            "gender": "Female",
            "age": 2,
            "weight": 4.5,
            "colour": "Naranja",
            "vaccinated": False
        }
]

menu = []
start = input('Iniciar? \n y/n \n>>>  ')

while 'y' in  start:

    print ("Busca los datos que necesites: \n 1- Nombre del gato \n 2-Vacunacion de los gatos \n 3-Estadisticas promedio \n 4-back")
    menu = input('>>>')

    if menu == "1":
        nombre=(input('nombre del gato \n >>>'))
        if nombre in miau_edd:
            print (miau_edd.sort (nombre))
        else:
            print ('Gato no encontrado')
    

        
    if menu == "2":
        if "vaccinated" in miau_edd:
            print ('los gatos vacunados son', miau_edd.sort (vaccinated=True))

    if menu == "3":
        print (miau_edd) 
    
    if "4" in menu: break