import requests

ciudad = input("Ciudad: ")
respuesta = requests.get(f"https://wttr.in/{ciudad}?format=3")
print(respuesta.text)
