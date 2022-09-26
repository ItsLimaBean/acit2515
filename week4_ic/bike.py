class Bike:
    def __init__(self):
        self.rider = None
        self.distance = 0
    
    def start_rental(self, driver):
        if self.rider is not None:
            raise RuntimeError(f"{self.rider} is already riding this bike")
        self.rider = driver

    def bike(self, distance):
        if distance < 0:
            raise AttributeError("distance needs to be a postive value")
        if not self.rider:
            raise RuntimeError("A rider is required before binking.")
        self.distance += distance
    
    def end_rental(self):
        if not self.rider:
            raise RuntimeError("Cannot end a rental that has not started")

        total_distance = self.distance
        self.rider = None
        self.distance = 0

        return total_distance
