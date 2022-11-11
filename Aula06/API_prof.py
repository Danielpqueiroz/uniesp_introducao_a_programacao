import requests
import json
import csv

API_KEY = 'c0a6c9f21eb7b95c3d7227ce9d0e6d0d'
LAT = ["38.7167","40.4165","43.2128","48.8534","51.5085"]
LOG = ["-9.1333","-3.7026","-75.4557","2.3488","-0.1257"]
for i in range(len(LAT)):
    url = (f"https://api.openweathermap.org/data/2.5/weather?lat={LAT[i]}&lon={LOG[i]}&appid={API_KEY}")

    resposta   = requests.request("GET", url)
    objetos    = json.loads(resposta.text)
    pais = objetos["sys"]["country"] 
    city = objetos["name"] 
    long = objetos["coord"] ["lon"]
    lat = objetos["coord"] ["lat"]
    print(f" {pais}, {city}, {long}, {lat}")
    
    file_name = './Aula06/writing.txt'
    with open(file_name, 'a') as file_object:
        file_object.write(f"{pais} , {city}, {long}, {lat}\n")

# for i in range(len(LAT)):

#     link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade[i]}&appid={API_KEY}&lang=pt_br&units=metric"

#     resposta   = requests.request("GET", link)
#     objetos    = json.loads(resposta.text)
#     pais = objetos["sys"]["country"] 
#     city = objetos["name"] 
#     long = objetos["coord"] ["lon"]
#     lat = objetos["coord"] ["lat"]
#     print(f" {pais}, {city}, {long}, {lat}")
    
#     file_name = './Aula06/writing.txt'
#     with open(file_name, 'a') as file_object:
#         file_object.write(f"{pais} , {city}, {long}, {lat}\n")     
# dados      = objetos['dados']

# for i in objetos:
#     print(f"{i} :: {objetos[i]}")


with open('./Aula06/writing.txt', "r") as file_object:
    #arquivo_csv = csv.reader(file_object, delimiter=",")
    cidade = file_object.readlines() 
for cidade in cidade:
    print(cidade.rstrip())
    