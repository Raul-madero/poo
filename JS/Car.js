class Car {
    constructor(license, driver) {
    this.id;
    this.license = license;
    this.driver = driver;
    this.passengers;
}
}
Car.prototype.printDataCar = function () {
    console.log(this.driver, this.driver.name, this.driver.document);
}