from car import Car


if __name__ == "__main__":
    car = Car()
    car.license = "AMS234"
    car.driver = "Andres Herrera"
    print(vars(car))