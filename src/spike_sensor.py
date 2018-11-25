from typing import Tuple
from abc import ABC, abstractmethod


class SpikeSensor(ABC):
    """Spike Sensor abstract class provides methods and interface to initialize and configure spike-shaped signal sensor
     data generators
     """

    def __init__(self, signal_width: Tuple = (5, 9), num_points: int=100, interval: int=15):
        self.signal_width = signal_width
        self.num_points = num_points
        self.interval = interval

    @property
    def signal_width(self) -> Tuple:
        """Defines a range of values on X-axis where the signal (a spike) will exist"""
        return self._signal_width

    @property
    def num_points(self) -> int:
        """Defines a number of iterations available for the generator before it exhausts"""
        return self._num_points

    @property
    def interval(self) -> int:
        """Defines an interval whitin which spikes will appear"""
        return self._interval

    @signal_width.setter
    def signal_width(self, width_tuple: Tuple):
        self._signal_width = width_tuple

    @num_points.setter
    def num_points(self, num_points: int):
        self._num_points = num_points

    @interval.setter
    def interval(self, interval:int):
        self._interval = interval

    @abstractmethod
    def signal_function(self, *args) -> int or float:
        """Abstract method allows for implementation of different signal shape functions (random, sin, etc.)
        Should return integer or float. Signal function variables that are passed through *args should be parsed in
         non-abstract signal_function method
        """
        pass

    def spike_data_generator(self, x: int=0) -> int or float:
        """Creates a generator object that yields spike-shaped signal sensor data"""
        for i in range(self.num_points):
            if(x >= self.signal_width[0]) & (x <= self.signal_width[1]):
                y = self.signal_function(x)
            else:
                y = 0
            if x >= self.interval:
                x = 0
            x += 1
            yield y



