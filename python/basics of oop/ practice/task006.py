# class variables


class Bike:
    rented_count = 0

    def __init__(self, brand, color, is_rented):
        self.brand = brand
        self.color = color
        self.is_rented = is_rented
    

    def rent(self):
        
        if self.is_rented == False:
            self.is_rented = True
            Bike.rented_count += 1
    def bike_return(self):
        if self.is_rented:
            self.is_rented = False
            Bike.rented_count -= 1

#
 

bike1 = Bike("bmw", "red", False)

bike2 = Bike("Giant", "blue", True)

bike1.rent()
bike1.rent()
 

bike2.rent()

print(Bike.rented_count)

bike1.bike_return()
print(Bike.rented_count)
