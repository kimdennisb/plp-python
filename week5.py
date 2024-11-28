class Smartphone:
    """Base class representing a generic smartphone."""
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life  # in hours
        self.__operating_system = "Android"  # Encapsulated attribute

    def install_app(self, app_name):
        """Simulate app installation."""
        print(f"{app_name} has been installed on {self.brand} {self.model}.")

    def charge_phone(self, hours):
        """Charge the phone and extend battery life."""
        self.battery_life += hours * 2  # Simplified charging logic
        print(f"Phone charged! Current battery life: {self.battery_life} hours.")

    def get_operating_system(self):
        """Get the operating system of the phone."""
        return self.__operating_system

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.battery_life}h battery life."


class GamingPhone(Smartphone):
    """Subclass representing a gaming smartphone."""
    def __init__(self, brand, model, storage, battery_life, cooling_system):
        super().__init__(brand, model, storage, battery_life)
        self.cooling_system = cooling_system  # e.g., "Liquid Cooling"

    def launch_game(self, game_name):
        """Simulate launching a game."""
        print(f"Launching {game_name} on {self.brand} {self.model} with {self.cooling_system}.")

    def charge_phone(self, hours):
        """Override to add faster charging for gaming phones."""
        self.battery_life += hours * 3
        print(f"Gaming phone charged quickly! Current battery life: {self.battery_life} hours.")


class CameraPhone(Smartphone):
    """Subclass representing a camera-centric smartphone."""
    def __init__(self, brand, model, storage, battery_life, camera_quality):
        super().__init__(brand, model, storage, battery_life)
        self.camera_quality = camera_quality  # e.g., "108 MP"

    def take_photo(self):
        """Simulate taking a high-quality photo."""
        print(f"Photo taken with {self.camera_quality} camera on {self.brand} {self.model}.")

    def edit_photo(self):
        """Simulate editing a photo."""
        print(f"Editing photo on {self.brand} {self.model}'s built-in editor.")


# Example Usage
if __name__ == "__main__":
    # Create a generic smartphone
    generic_phone = Smartphone("GenericBrand", "X100", 128, 20)
    print(generic_phone)
    generic_phone.install_app("WhatsApp")
    generic_phone.charge_phone(2)

    # Create a gaming phone
    gaming_phone = GamingPhone("GameX", "UltraPro", 256, 15, "Liquid Cooling")
    print(gaming_phone)
    gaming_phone.launch_game("Cyber Racing")
    gaming_phone.charge_phone(1)

    # Create a camera phone
    camera_phone = CameraPhone("PhotoX", "VisionMax", 128, 18, "108 MP")
    print(camera_phone)
    camera_phone.take_photo()
    camera_phone.edit_photo()
    
    
class Vehicle:
    """Base class representing a generic vehicle."""
    def move(self):
        """Generic move method, meant to be overridden by subclasses."""
        print("The vehicle moves in its own way.")

class Car(Vehicle):
    """Subclass representing a car."""
    def move(self):
        """Override move method to simulate driving."""
        print("Driving 🚗")

class Plane(Vehicle):
    """Subclass representing a plane."""
    def move(self):
        """Override move method to simulate flying."""
        print("Flying ✈️")

class Boat(Vehicle):
    """Subclass representing a boat."""
    def move(self):
        """Override move method to simulate sailing."""
        print("Sailing 🛥️")

class Bicycle(Vehicle):
    """Subclass representing a bicycle."""
    def move(self):
        """Override move method to simulate pedaling."""
        print("Pedaling 🚴‍♂️")

# Example usage of polymorphism
if __name__ == "__main__":
    # List of vehicle objects
    vehicles = [Car(), Plane(), Boat(), Bicycle()]

    # Demonstrate polymorphism
    for vehicle in vehicles:
        vehicle.move()

