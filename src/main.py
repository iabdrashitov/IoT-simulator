from src.random_spike_sensor import RandomSpikeSensor
import time

if __name__=="__main__":
    sensor = RandomSpikeSensor(random_interval=(0.0, 0.0))
    generator = sensor.spike_data_generator()
    for i in range(50):
        time.sleep(0.3)
        sensor_output = next(generator)
        print("Sensor output value: {0}".format(sensor_output))
