import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("HTTP_REQUEST")

headers = {
    "Authorization": "Bearer "+os.getenv("USER_AUTH_TOKEN"),
    "Content-Type": "application/json"
}

body = {
  "messaging_product": "whatsapp",
  "to": os.getenv("TEST_PHONE_NUMBER"),
  "type": "template",
  "template": {
      "name": "hello_world",
      "language": {
          "code": "en_US"
      }
  }
}

response = requests.post(url, headers=headers, data=json.dumps(body))

if response.status_code == 200:
    data = response.json() # response JSON
    print("Resposta bem-sucedida:", data)
else:
    print("Erro na solicitação. Código de status:", response.status_code)
    print("Conteúdo da resposta:", response.text)