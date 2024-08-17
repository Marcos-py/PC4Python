# Este programa hace lo siguiente:
# Solicita al usuario que ingrese la cantidad de bitcoins que posee.
# Consulta la API de CoinDesk para obtener el precio actual del Bitcoin en USD.
# Calcula el valor total de los bitcoins del usuario en USD y lo muestra con cuatro decimales, 
# usando comas como separadores de miles.

import requests

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return data['bpi']['USD']['rate_float']
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        return None

def main():
    try:
        n = float(input("Ingrese la cantidad de bitcoins que posee: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    bitcoin_price = get_bitcoin_price()
    if bitcoin_price is not None:
        total_value = n * bitcoin_price
        print(f"El costo actual de {n} Bitcoins en USD es: ${total_value:,.4f}")

if __name__ == "__main__":
    main()