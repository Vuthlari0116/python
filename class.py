class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def make_call(self, number):
        return f"Dialing {number} from {self.brand} {self.model}..."

    def send_message(self, number, message):
        return f"Sending message to {number}: {message}"

    def __str__(self):
        return f"{self.brand} {self.model} priced at ${self.price}"


# Inheritance: A specialized class for Gaming Smartphones
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu, cooling_system):
        super().__init__(brand, model, price)
        self.gpu = gpu
        self.cooling_system = cooling_system

    def play_game(self, game_name):
        return f"Playing {game_name} on {self.brand} {self.model} with {self.gpu} GPU."

    def __str__(self):
        return f"{self.brand} {self.model} (Gaming Edition) with {self.gpu} GPU and {self.cooling_system} cooling system, priced at ${self.price}"


# Example usage
if __name__ == "__main__":
    phone = Smartphone("Apple", "iPhone 14", 999)
    gaming_phone = GamingSmartphone("ASUS", "ROG Phone 7", 1299, "Adreno 730", "Vapor Chamber")

    print(phone)
    print(phone.make_call("123-456-7890"))
    print(phone.send_message("123-456-7890", "Hello!"))

    print(gaming_phone)
    print(gaming_phone.play_game("Genshin Impact"))