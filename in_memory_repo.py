class InMemoryRepo:

    def __init__(self):
        self.drivers = []

        f1_drivers_2025 = [
            {"name": "Max Verstappen", "team": "Red Bull Racing", "number": 1, "skill_level": 98},
            {"name": "Liam Lawson", "team": "Red Bull Racing", "number": 30, "skill_level": 85},
            {"name": "Lewis Hamilton", "team": "Ferrari", "number": 44, "skill_level": 95},
            {"name": "Charles Leclerc", "team": "Ferrari", "number": 16, "skill_level": 92},
            {"name": "George Russell", "team": "Mercedes", "number": 63, "skill_level": 90},
            {"name": "Andrea Kimi Antonelli", "team": "Mercedes", "number": 12, "skill_level": 80},
            {"name": "Lando Norris", "team": "McLaren", "number": 4, "skill_level": 88},
            {"name": "Oscar Piastri", "team": "McLaren", "number": 81, "skill_level": 86},
            {"name": "Fernando Alonso", "team": "Aston Martin", "number": 14, "skill_level": 87},
            {"name": "Lance Stroll", "team": "Aston Martin", "number": 18, "skill_level": 75},
            {"name": "Pierre Gasly", "team": "Alpine", "number": 10, "skill_level": 82},
            {"name": "Jack Doohan", "team": "Alpine", "number": 7, "skill_level": 78},
            {"name": "Alexander Albon", "team": "Williams", "number": 23, "skill_level": 80},
            {"name": "Carlos Sainz Jr.", "team": "Williams", "number": 55, "skill_level": 84},
            {"name": "Nico Hulkenberg", "team": "Sauber", "number": 27, "skill_level": 77},
            {"name": "Gabriel Bortoleto", "team": "Sauber", "number": 5, "skill_level": 70},
            {"name": "Esteban Ocon", "team": "Haas", "number": 31, "skill_level": 79},
            {"name": "Oliver Bearman", "team": "Haas", "number": 87, "skill_level": 72},
            {"name": "Yuki Tsunoda", "team": "Racing Bulls", "number": 22, "skill_level": 76},
            {"name": "Isack Hadjar", "team": "Racing Bulls", "number": 6, "skill_level": 68}
        ]

        for driver in f1_drivers_2025:
            self.add(driver)

    def add(self, driver):
        self.drivers.append(driver)
        return driver

    def find(self, number):
        for driver in self.drivers:
            if driver["number"] == number:
                return driver
        return None

    def remove(self, number):
        old_driver = self.find(number)
        if old_driver is None:
            return None
        self.drivers.remove(old_driver)
        return old_driver

    def update(self, new_driver):
        old_driver = self.remove(new_driver["number"])
        if old_driver is None:
            return None
        return self.add(new_driver)

    def get_all(self):
        return self.drivers


