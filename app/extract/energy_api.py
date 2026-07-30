from datetime import datetime

def get_energy_price():
    """
    Simulates retrieving energy market data.
    """

    data = {
        "timestamp": datetime.now(),
        "market": "European Energy Market",
        "price": 102.5,
        "currency": "EUR/MWh"
    }

    return data