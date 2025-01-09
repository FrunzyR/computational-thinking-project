import json
from io import StringIO

import pandas as pd

class FileRepo:
    def __init__(self):
        self.data = pd.read_csv('drivers.csv')
        self.remove_weird_pandas_columns()
        self.drivers = json.loads(self.data.to_json(orient='records'))
        self.write_file()

    def get_all(self):
        return self.drivers

    def find(self, number):
        for driver in self.drivers:
            if driver["number"] == number:
                return driver
        return None


    def add(self, driver):
        self.drivers.append(driver)
        self.write_file()
        return driver


    def update(self, new_driver):
        old_driver = self.remove(new_driver["number"])
        if old_driver is None:
            return None
        self.write_file()
        return self.add(new_driver)


    def remove(self, number):
        old_driver = self.find(number)
        if old_driver is None:
            return None
        self.drivers.remove(old_driver)
        self.write_file()
        return old_driver

    def write_file(self):
        self.data = pd.read_json(StringIO(json.dumps(self.drivers)), orient='records')
        self.data.to_csv('drivers.csv', index=False)

    def remove_weird_pandas_columns(self):
        self.data.drop(self.data.columns[self.data.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
