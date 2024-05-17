import mercadopago

def attPrefferences():
    sdk = mercadopago.SDK("APP_USR-5859714400275253-050710-e6ede001af555236613cfc606515b533-813143227")
         
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