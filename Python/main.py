from car import Car
from account import Account


if __name__ == "__main__":
    car = Car("AMS234", Account("Andres Herrera", "ANDA7894"))
    print(vars(car))
    print(vars(car.driver))