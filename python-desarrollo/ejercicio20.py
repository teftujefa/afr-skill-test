import requests

def obtener_post():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        if response.status_code == 200:
            data = response.json()
            print("Título: " + data["title"])
    except Exception:
        print("Error al obtener el post")

obtener_post()