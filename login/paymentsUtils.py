import mercadopago
from dotenv import load_dotenv
from pathlib import os

def attPrefferences(person_type, quantity = 1):
    load_dotenv()
    
    if person_type == 1:
        value = 70.0
    if person_type == 2:
        value = 90.0
    if person_type == 3:
        value = 120.0
    
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
    
    
    sdk = mercadopago.SDK('APP_USR-3755386082060312-050219-532f45efc4eacac399ab6713407966b5-1792061375')
         
    preference_data = {
        "items": [
            {
                "id":"mini-courses-0",
                "title": "Inscrição Mini Cursos",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": total
            },
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
            "success": "https://eventocoama.com.br/auth/success",
            "failure": "https://eventocoama.com.br/auth/failure",
            "pending": "https://eventocoama.com.br/auth/pendings"
        },
        "auto_return": "approved",
    }

    preference_response = sdk.preference().create(preference_data)
    return preference_response["response"]["id"]