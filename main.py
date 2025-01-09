from crypt import methods

from flask import Flask, request, make_response

from file_repo import FileRepo
from in_memory_repo import InMemoryRepo
from circuit_memory_repo import CircuitMemoryRepo

app = Flask(__name__)

drivers = []
repo = FileRepo()

circuits = []
repo_circuit = CircuitMemoryRepo()

def f1_time_to_milliseconds(f1_time):
    f1_time = f1_time.replace(':', '.')
    f1_time = f1_time.split('.')
    milliseconds_fastest_lap = int(f1_time[0])*60*1000 + int(f1_time[1])*1000 +int(f1_time[2])
    return milliseconds_fastest_lap


@app.route('/driver', methods=['GET'])
def get_drivers():
    return repo.get_all()

@app.route('/driver', methods=['POST'])
def add_driver():
    if repo.find(int(request.json["round"])):
        return "Number already exists", 400
    repo.add(request.json)
    return "Driver added", 200


@app.route('/driver', methods=['PUT'])
def update_driver():
    driver = repo.update(request.json)
    if driver:
        return "Driver updated", 200
    return "Driver not found", 404


@app.route('/driver', methods=['DELETE'])
def remove_driver():
    old_driver = repo.remove(int(request.args.get("number")))
    if old_driver:
        return "Driver removed", 200
    return "Driver not found", 404


@app.route('/driver/search', methods=['GET'])
def search_driver():
    matching_drivers = []
    all_drivers = repo.get_all()
    for driver in all_drivers:
        if request.args.get("key").lower() in driver["name"].lower():
            matching_drivers.append(driver)
    return matching_drivers


@app.route('/driver/filter', methods=['GET'])
def filter_driver():
    matching_drivers = []
    all_drivers = repo.get_all()
    lower = int(request.args.get("lower"))
    upper = int(request.args.get("upper"))
    for driver in all_drivers:
        if lower <= driver["skill_level"] <= upper:
            matching_drivers.append(driver)
    return matching_drivers


@app.route('/driver/sort', methods=['GET'])
def sort_driver():
    all_drivers = repo.get_all()
    return sorted(all_drivers, key=lambda driver: driver['skill_level'])

@app.route('/circuit', methods=['GET'])
def get_all_circuits():
    return repo_circuit.get_all()

@app.route('/circuit', methods=['POST'])
def add_circuit():
    if repo_circuit.find(int(request.json["round"])):
        return "This circuit already exists", 400
    repo_circuit.add(request.json)
    return "Circuit added", 200

@app.route('/circuit', methods=['PUT'])
def update_circuit():
    circuit = repo_circuit.update_circuit(request.json)
    if circuit:
        return "Already updated", 200
    return "Circuit not found", 400

@app.route('/circuit', methods=['DELETE'])
def remove_circuit():
    old_driver = repo_circuit.remove(int(request.args.get("round")))
    if old_driver:
        return "Circuit removed", 200
    return "Circuit not found", 404

@app.route('/circuit/search', methods=['GET'])
def search_circuit():
    matching_circuit = []
    all_circuits = repo_circuit.get_all()
    for circuit in all_circuits:
        if request.args.get("key").lower() in circuit["circuit"].lower():
            matching_circuit.append(circuit)
    return matching_circuit

@app.route('/circuit/filter', methods=["GET"])
def filter_circuit():
    matching_circuits = []
    all_circuits = repo_circuit.get_all()
    lower = float(request.args.get("lower"))
    upper = float(request.args.get("upper"))
    for circuit in all_circuits:
        if lower <= circuit["length_km"] <= upper:
            matching_circuits.append(circuit)
    return matching_circuits

@app.route('/circuit/sort', methods=["GET"])
def sort_circuit_time():
    all_circuits = repo_circuit.get_all()
    return sorted(all_circuits, key=lambda circuit:f1_time_to_milliseconds(circuit["fastest_lap"]))


if __name__ == '__main__':
    app.run(port=5001, debug=True)