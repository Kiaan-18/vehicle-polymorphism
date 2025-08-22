class BMW:
    def brand(self):
        print("This is a BMW")
    def speed(self):
        print("Top speed: 250km/h")
    def price(self):
        print("BMW price: $70.000")
class Ferrari:
    def brand(self):
        print("This is a ferrari")
    def speed(self):
        print("Top speed 340km/h")
    def price(self):
        print("Ferrari price:$250.000")
def car_details(car):
    car.brand()
    car.speed()
    car.price()
bmw_car=BMW()
ferrari_car=Ferrari()
print("BMW Details:")
car_details(bmw_car)
print("\n Ferrari Details:")
car_details(ferrari_car)
