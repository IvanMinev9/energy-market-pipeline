from app.config.settings import APP_NAME
from app.extract.energy_api import get_energy_price

def main():

    print(APP_NAME)

    energy_data = get_energy_price()

    print(energy_data)

if __name__ == "__main__":
    main()

