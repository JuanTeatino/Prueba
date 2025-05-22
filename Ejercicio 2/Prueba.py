import requests
from bs4 import BeautifulSoup


palabra = input("Ingrese la palabra clave: ")

url = f"https://listado.mercadolibre.com.co/{palabra.replace(' ', '-')}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    productos = soup.find_all("li", class_="ui-search-layout__item")

    print(f"\nResultados para: {palabra}\n")

    for i, producto in enumerate(productos[:5]):
        titulo_tag = producto.find("h2", class_="ui-search-item__title")
        precio_tag = producto.find("span", class_="andes-money-amount__fraction")

        titulo = titulo_tag.text.strip() if titulo_tag else "Sin título"
        precio = precio_tag.text.strip() if precio_tag else "Sin precio"

        print(f"{i+1}. {titulo} - ${precio}")
else:
    print("Error al acceder a Mercado Libre.")