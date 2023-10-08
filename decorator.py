import abc

class Beverage(abc.ABC):
    def __init__(self):
        self.description = "Unknown Beverage"
    
    def get_description(self):
        return self.description
    
    @abc.abstractmethod
    def cost(self):
        pass


class AddonDecorator(Beverage):
    def __init__(self, b: Beverage):
        self.beverage = b
    

class CaramelDecorator(AddonDecorator):
    def get_description(self):
        return self.beverage.get_description() + " Caramel"
    
    def cost(self):
        return self.beverage.cost() + 1
    
class SyrupDecorator(AddonDecorator):
    def get_description(self):
        return self.beverage.get_description + " Syrup"
    
    def cost(self):
        return self.beverage.cost() + 2


class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"
    
    def cost(self):
        return 1

class Latte(Beverage):
    def __init__(self):
        self.description = "Latte"
    
    def cost(self):
        return 2


if __name__ == "__main__":
    latte: Latte = Latte()
    espesso: Espresso = Espresso()
    new_latte:Latte = CaramelDecorator(CaramelDecorator(latte))
    print(CaramelDecorator(CaramelDecorator(latte)).cost())
    print(new_latte.get_description())
    