import mercadopago
from dotenv import load_dotenv
from pathlib import os

def attPrefferences(person_type, quantity = 1):
    load_dotenv()
    
    if person_type == 1:
        value = 50.0
    if person_type == 2:
        value = 70.0
    if person_type == 3:
        value = 100.0
    
    value = value * quantity
    
    sdk = mercadopago.SDK('APP_USR-3755386082060312-050219-532f45efc4eacac399ab6713407966b5-1792061375')
         
    preference_data = {
        "items": [
            {
                "id":"camisa-lg-id",
                "title": "Congresso COAMA",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": value
            }
        ],
        "back_urls": {
            "success": "https://eventocoama.com.br/auth/success",
            "failure": "https://eventocoama.com.br/auth/failure",
            "pending": "https://eventocoama.com.br/auth/pendings"
        },
        "auto_return": "approved",
    }

    preference_response = sdk.preference().create(preference_data)
    return preference_response["response"]["id"]

def getCoursePrefferences(total):
    try:
        sdk = mercadopago.SDK('APP_USR-3755386082060312-050219-532f45efc4eacac399ab6713407966b5-1792061375')
        
        preference_data = {
            "items": [
                {
                    "id": "mini-courses-0",
                    "title": "Inscrição Mini Cursos",
                    "quantity": 1,
                    "currency_id": "BRL",
                    "unit_price": total
                },
            ],
            "back_urls": {
                "success": "https://eventocoama.com.br/auth/subscription-success",
                "failure": "https://eventocoama.com.br/auth/failure",
                "pending": "https://eventocoama.com.br/auth/pendings"
            },
            "auto_return": "approved",
        }


        preference_response = sdk.preference().create(preference_data)

        print("Resposta da API:", preference_response)
        

        if 'response' in preference_response and 'id' in preference_response['response']:
            return preference_response['response']['id']
        else:
           
            raise ValueError(f"A resposta da API não contém a chave 'id'. Resposta: {preference_response}")
    
    except Exception as e:
        print(f"Ocorreu um erro ao criar a preferência: {e}")
        raise

def getCoursePrefferencesDesconto(total):
    
    
    sdk = mercadopago.SDK('APP_USR-3755386082060312-050219-532f45efc4eacac399ab6713407966b5-1792061375')
         
    preference_data = {
        "items": [
            {
                "id":"mini-courses-0",
                "title": "Inscrição no Evento + Mini Cursos ",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": total
            },
        ],
        "back_urls": {
            "success": "https://eventocoama.com.br/auth/payment-subscription-success",
            "failure": "https://eventocoama.com.br/auth/failure",
            "pending": "https://eventocoama.com.br/auth/pendings"
        },
        "auto_return": "approved",
    }

    preference_response = sdk.preference().create(preference_data)
    return preference_response["response"]["id"]

def getCoursePrefferencesDescontoCombo(total):
    
    
    sdk = mercadopago.SDK('APP_USR-3755386082060312-050219-532f45efc4eacac399ab6713407966b5-1792061375')
         
    preference_data = {
        "items": [
            {
                "id":"mini-courses-0",
                "title": "COMBO de 5 pessoas: Evento + Minicursos ",
                "quantity": 5,
                "currency_id": "BRL",
                "unit_price": total
            },
        ],
        "back_urls": {
            "success": "https://eventocoama.com.br/auth/payment-subscription-combo-success",
            "failure": "https://eventocoama.com.br/auth/failure",
            "pending": "https://eventocoama.com.br/auth/pendings"
        },
        "auto_return": "approved",
    }

    

    preference_response = sdk.preference().create(preference_data)
    return preference_response["response"]["id"]

