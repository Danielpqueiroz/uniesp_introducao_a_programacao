import requests

API_KEY = "c0a6c9f21eb7b95c3d7227ce9d0e6d0d"
cidade = ["lisboa","madrid","roma","paris","londres"]


for i in range(len(cidade)):
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade[i]}&appid={API_KEY}&lang=pt_br&units=metric"

    requisicao = requests.get(link)
    requisicao.dic = requisicao.json()
    #print(requisicao.dic)
    pais = requisicao.dic["sys"]["country"] 
    city = requisicao.dic["name"] 
    long = requisicao.dic["coord"] ["lon"]
    lat = requisicao.dic["coord"] ["lat"]
    # print(f"{descricao}, {temperatura:.2f}°C, {pais}, {city}, {long}, {lat}")
    print(f" {pais}, {city}, {long}, {lat}")

    file_name = './Aula06/writing.txt'
    with open(file_name, 'a') as file_object:
        file_object.write(f"{pais} , {city}, {long}, {lat}\n")


    # file_object.write("Eu amo programar em SQL!\n")
    # file_object.write("Eu amo programar em Python!\n")
# descricao = requisicao.dic["weather"][0]["description"]f
# temperatura = requisicao.dic["main"]["temp"] 

