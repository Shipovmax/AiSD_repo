class BacteriaProducer:
    def __init__(self, max_bacteria):
        # Set the maximum limit.
        self.max_bacteria = max_bacteria
        # The current quantity is 0 by default.
        self.current_bacteria = 0

    def create_new(self):
        if self.current_bacteria < self.max_bacteria:
            self.current_bacteria += 1
            print(
                f"One bacterium was added. Bacteria in the population: {self.current_bacteria}"
            )
        else:
            print("There is no room for a new bacterium")

    def remove_one(self):
        if self.current_bacteria > 0:
            self.current_bacteria -= 1
            print(
                f"One bacterium was removed. Bacteria in the population: {self.current_bacteria}"
            )
        else:
            print("There are no bacteria in the population, nothing can be removed")


# Usage example
bacteria_producer = BacteriaProducer(max_bacteria=3)
bacteria_producer.remove_one()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.remove_one()
