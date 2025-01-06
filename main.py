from flask import Flask, request, make_response

from in_memory_repo import InMemoryRepo

app = Flask(__name__)

drivers = []
repo = InMemoryRepo()

@app.route('/driver', methods=['GET'])
def get_drivers():
    return repo.get_all()

@app.route('/driver', methods=['POST'])
def add_driver():
    if repo.find(request.json["number"]):
        return "Number already exist", 400
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


if __name__ == '__main__':
    app.run(port=5001, debug=True)