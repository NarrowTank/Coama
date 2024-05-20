import mercadopago
from dotenv import load_dotenv
from pathlib import os

def attPrefferences():
    load_dotenv()
    
    sdk = mercadopago.SDK(str(os.getenv('MP_ACCESS_TOKEN')))
         
    preference_data = {
        "items": [
            {
                "id":"camisa-lg-id",
                "title": "CAMISAS LG",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": 1.0
            }
        ]
    }

    preference_response = sdk.preference().create(preference_data)
    return preference_response["response"]["id"]