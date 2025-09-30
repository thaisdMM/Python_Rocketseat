# o Modulo de terceiro não faz parte do conjuto padrao do python 
# - nesse exemplo vamos instalar com comando pip a biblioteca request 
# - pip3 install requests==2.31.0 
# - detalhe instalei uma versao mais nova, mas a de cima é a do professor

print(f"\nImportação e uso de um módulo de terceiros")
import requests

# falar o site que quer receber os dados:
url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitação http para {url} restornou o status {response.status_code}")

# a respota do terminal foi:
# Importação e uso de um módulo de terceiros
# Solicitação http para https://www.example.com restornou o status 200
