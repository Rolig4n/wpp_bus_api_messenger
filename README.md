# wpp_bus_api_messenger
Repositório de estudo sobre API da Meta

## Executar
>```python main.py```

## Passo a passo de configuração
- **Token de acesso**: fornecido pela conta de desenvolvedor da meta.
  tambem pode ser obtido pela conta que gerencia os apps da Empresa
- **Números de telefone**: são necessários dois números, o de origem e o destinatário
  o de origem é configurado na plataforma da Meta, nos dados da Empresa
> No código exemplo, está sendo utilizado como destinatário o número de telefone do autor do código

## Estrutura da chamada
- O tipo de requisição realizada é do tipo **POST**, eo link da API para enviar mensagens é o
  ``https://graph.facebook.com/v18.0/193513790520352/messages``
- O cabeçalho da requisição conten dois marcadores, um de contudo e o de autoriuzação
  ```
  Content-Type: application/json
  Authorization: Bearer TOKEN
  ```
- E por ultimo, o corpo do request:
  ```JSON
  {
    "messaging_product": "whatsapp",
    "to": "5517996329748",
    "type": "template",
    "template": {
        "name": "hello_world",
        "language": {
            "code": "en_US"
        }
    }
  }
  ```
## Resultado da chamada
- Caso a reposta seja favoravel, o resultado esperado é o seguinte:
  ```JSON
  {
    "messaging_product": "whatsapp",
    "contacts": [
        {
            "input": "5517996329748",
            "wa_id": "5517996329748"
        }
    ],
    "messages": [
        {
            "id": "wamid.HBgNNTUxNzk5NjMyOTc0OBUCABEYEjI3NjVGRUMyRUMwNDhBQjUwQgA=",
            "message_status": "accepted"
        }
    ]
  }
  ```
- Formatos de resposta para erros comuns:
> 401 Unauthorized 
>```JSON
>  {
>    "error": {
>        "message": "Malformed access token",
>        "type": "OAuthException",
>        "code": 190,
>        "fbtrace_id": "AwVEzPpKukEine_Vl5BtkUI"
>    }
>  }
>```
>400 Bad Request
>```JSON
> {
>    "error": {
>        "message": "(#131030) Recipient phone number not in allowed list",
>        "type": "OAuthException",
>        "code": 131030,
>        "error_data": {
>            "messaging_product": "whatsapp",
>            "details": "O número de telefone do destinatário não está na lista de permissão: Adicione o telefone do destinatário à lista de destinatários e tente novamente."
>        },
>        "fbtrace_id": "Ac-kD15x8drIxMSGvx8ZwVA"
>    }
>}
> ```
