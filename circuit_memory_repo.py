class CircuitMemoryRepo:
    def __init__(self):
        self.circuits = []

        f1_circuits_2025 =  [
    {"round": 1, "circuit": "Albert Park Circuit", "fastest_lap": "1:20.235", "length_km": 5.278},
    {"round": 2, "circuit": "Shanghai International Circuit", "fastest_lap": "1:32.238", "length_km": 5.451},
    {"round": 3, "circuit": "Suzuka International Racing Course", "fastest_lap": "1:30.983", "length_km": 5.807},
    {"round": 4, "circuit": "Bahrain International Circuit", "fastest_lap": "1:31.447", "length_km": 5.412},
    {"round": 5, "circuit": "Jeddah Corniche Circuit", "fastest_lap": "1:27.478", "length_km": 6.174},
    {"round": 6, "circuit": "Miami International Autodrome", "fastest_lap": "1:29.708", "length_km": 5.412},
    {"round": 7, "circuit": "Autodromo Enzo e Dino Ferrari (Imola)", "fastest_lap": "1:15.484", "length_km": 4.909},
    {"round": 8, "circuit": "Circuit de Monaco", "fastest_lap": "1:12.909", "length_km": 3.337},
    {"round": 9, "circuit": "Circuit de Barcelona-Catalunya", "fastest_lap": "1:18.149", "length_km": 4.657},
    {"round": 10, "circuit": "Circuit Gilles Villeneuve", "fastest_lap": "1:13.078", "length_km": 4.361},
    {"round": 11, "circuit": "Red Bull Ring", "fastest_lap": "1:05.619", "length_km": 4.318},
    {"round": 12, "circuit": "Silverstone Circuit", "fastest_lap": "1:27.097", "length_km": 5.891},
    {"round": 13, "circuit": "Circuit de Spa-Francorchamps", "fastest_lap": "1:46.286", "length_km": 7.004},
    {"round": 14, "circuit": "Hungaroring", "fastest_lap": "1:17.497", "length_km": 4.381},
    {"round": 15, "circuit": "Circuit Zandvoort", "fastest_lap": "1:11.097", "length_km": 4.259},
    {"round": 16, "circuit": "Autodromo Nazionale Monza", "fastest_lap": "1:21.046", "length_km": 5.793},
    {"round": 17, "circuit": "Marina Bay Street Circuit", "fastest_lap": "1:41.905", "length_km": 4.940},
    {"round": 18, "circuit": "Circuit of the Americas", "fastest_lap": "1:37.330", "length_km": 5.513},
    {"round": 19, "circuit": "Autódromo Hermanos Rodríguez", "fastest_lap": "1:17.774", "length_km": 4.304},
    {"round": 20, "circuit": "Interlagos Circuit", "fastest_lap": "1:10.540", "length_km": 4.309},
    {"round": 21, "circuit": "Las Vegas Street Circuit", "fastest_lap": "1:34.876", "length_km": 6.120},
    {"round": 22, "circuit": "Yas Marina Circuit", "fastest_lap": "1:26.103", "length_km": 5.554}
]

        for circuit in f1_circuits_2025:
            self.add(circuit)

    def add(self, circuit):
        self.circuits.append(circuit)
        return circuit

    def find(self, round):
        for circuit in self.circuits:
            if circuit["round"] == round:
                return circuit
        return None

    def remove(self, round):
        old_circuit = self.find(round)
        if old_circuit is None:
            return None
        self.circuits.remove(old_circuit)
        return old_circuit

    def update_circuit(self, new_circuit):
        old_circuit = self.remove(new_circuit["round"])
        return self.add(new_circuit) if old_circuit else None

    def get_all(self):
        return self.circuits