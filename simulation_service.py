import random

class SimulationService:
    def __init__(self):
        pass

    def f1_time_to_milliseconds(self, f1_time):
        f1_time = f1_time.replace(':', '.')
        f1_time = f1_time.split('.')
        milliseconds_fastest_lap = int(f1_time[0]) * 60 * 1000 + int(f1_time[1]) * 1000 + int(f1_time[2])
        return milliseconds_fastest_lap

    def generate_lap_time(self, fastest_lap, skill_level):
        return fastest_lap + (100 - int(skill_level)) * 10 - random.randint(-100, 100)

    def simulate_lap_result(self, drivers, fastest_lap):
        drivers_name = []
        fastest_lap = self.f1_time_to_milliseconds(fastest_lap)
        times = []
        for driver in drivers:
            drivers_name.append(driver["name"])
            times.append(self.generate_lap_time(fastest_lap, driver["skill_level"]))
        return drivers_name, times