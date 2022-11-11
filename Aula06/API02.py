import requests

API_KEY = "c0a6c9f21eb7b95c3d7227ce9d0e6d0d"
cep = "58051-570"
cidade = "br"
link = f"https://api.openweathermap.org/data/2.5/weather?zip=94040,us&appid={API_KEY}"

requisicao = requests.get(link)
requisicao.dic = requisicao.json()
print(requisicao.dic)
# descricao = requisicao.dic["weather"][0]["description"]
# temperatura = requisicao.dic["main"]["temp"] 
pais = requisicao.dic["sys"]["country"] 
city = requisicao.dic["name"] 
long = requisicao.dic["coord"] ["lon"]
lat = requisicao.dic["coord"] ["lat"]
# print(f"{descricao}, {temperatura:.2f}°C, {pais}, {city}, {long}, {lat}")
print(f" {pais}, {city}, {long}, {lat}")