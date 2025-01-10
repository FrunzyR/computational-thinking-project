from crypt import methods

from flask import Flask, request

from circuit_memory_repo import CircuitMemoryRepo
from file_repo import FileRepo
from simulation_service import SimulationService

app = Flask(__name__)

driver_repo = FileRepo()
circuit_repo = CircuitMemoryRepo()

sim_service = SimulationService()

@app.route('/driver', methods=['GET'])
def get_drivers():
    return driver_repo.get_all()

@app.route('/driver', methods=['POST'])
def add_driver():
    if driver_repo.find(int(request.json["number"])):
        return "Number already exists", 400
    driver_repo.add(request.json)
    return "Driver added", 200


@app.route('/driver', methods=['PUT'])
def update_driver():
    driver = driver_repo.update(request.json)
    if driver:
        return "Driver updated", 200
    return "Driver not found", 404


@app.route('/driver', methods=['DELETE'])
def remove_driver():
    old_driver = driver_repo.remove(int(request.args.get("number")))
    if old_driver:
        return "Driver removed", 200
    return "Driver not found", 404


@app.route('/driver/search', methods=['GET'])
def search_driver():
    matching_drivers = []
    all_drivers = driver_repo.get_all()
    for driver in all_drivers:
        if request.args.get("key").lower() in driver["name"].lower():
            matching_drivers.append(driver)
    return matching_drivers


@app.route('/driver/filter', methods=['GET'])
def filter_driver():
    matching_drivers = []
    all_drivers = driver_repo.get_all()
    lower = int(request.args.get("lower"))
    upper = int(request.args.get("upper"))
    for driver in all_drivers:
        if lower <= driver["skill_level"] <= upper:
            matching_drivers.append(driver)
    return matching_drivers


@app.route('/driver/sort', methods=['GET'])
def sort_driver():
    all_drivers = driver_repo.get_all()
    return sorted(all_drivers, key=lambda driver: int(driver['skill_level']))

@app.route('/circuit', methods=['GET'])
def get_all_circuits():
    return circuit_repo.get_all()

@app.route('/circuit', methods=['POST'])
def add_circuit():
    if circuit_repo.find(int(request.json["round"])):
        return "This circuit already exists", 400
    circuit_repo.add(request.json)
    return "Circuit added", 200

@app.route('/circuit', methods=['PUT'])
def update_circuit():
    circuit = circuit_repo.update_circuit(request.json)
    if circuit:
        return "Already updated", 200
    return "Circuit not found", 400

@app.route('/circuit', methods=['DELETE'])
def remove_circuit():
    old_driver = circuit_repo.remove(int(request.args.get("round")))
    if old_driver:
        return "Circuit removed", 200
    return "Circuit not found", 404

@app.route('/circuit/search', methods=['GET'])
def search_circuit():
    matching_circuit = []
    all_circuits = circuit_repo.get_all()
    for circuit in all_circuits:
        if request.args.get("key").lower() in circuit["circuit"].lower():
            matching_circuit.append(circuit)
    return matching_circuit

@app.route('/circuit/filter', methods=["GET"])
def filter_circuit():
    matching_circuits = []
    all_circuits = circuit_repo.get_all()
    lower = float(request.args.get("lower"))
    upper = float(request.args.get("upper"))
    for circuit in all_circuits:
        if lower <= circuit["length_km"] <= upper:
            matching_circuits.append(circuit)
    return matching_circuits

@app.route('/circuit/sort', methods=["GET"])
def sort_circuit_time():
    all_circuits = circuit_repo.get_all()
    return sorted(all_circuits, key=lambda circuit:sim_service.f1_time_to_milliseconds(circuit["fastest_lap"]))

@app.route('/result_simulate', methods=['GET'])
def generate_result():
    circuit_id = request.args.get("round")
    circuit = circuit_repo.find(int(circuit_id))
    fastest_lap = circuit["fastest_lap"]
    drivers = driver_repo.get_all()

    result = sim_service.simulate_lap_result(drivers, fastest_lap)
    result = zip(result[0], result[1])
    result = sorted(result, key=lambda entry:entry[1])
    return {"drivers_names": [x[0] for x in result], "results": [x[1] for x in result]}

if __name__ == '__main__':
    app.run(port=5001, debug=True)