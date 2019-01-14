import random
from src.spike_sensor import SpikeSensor


class RandomSpikeSensor(SpikeSensor):
    def __init__(self, random_interval):
        self.random_interval = random_interval
        super().__init__()

    def signal_function(self, *args):
        x = args[0]
        return x + random.randint(self.random_interval[0], self.random_interval[1])