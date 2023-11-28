#---------------------------------------
# Simple json wrapper
#
# This file specifically handles file I/O
#
#-----------------------------------------

import json
import csv
import os

class JsonObj:
    # Best to leave file_path empty and load data when necessary, but give the option
    def __init__(self, file_path=None):
        self.file_path = file_path
        self.data = None
        if self.file_path:
            self.load_data()

    def __load_from_json(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8', errors='replace') as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading JSON from file: {e}")

    def __load_from_csv(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8', errors='replace') as file:
                csv_reader = csv.DictReader(file)
                self.data = list(csv_reader)
        except (FileNotFoundError, csv.Error) as e:
            print(f"Error loading CSV from file: {e}")
        
    def __load_from_file(self):
        try:
            if self.file_path:
                file_name, file_ext = os.path.splitext(self.file_path)
                file_ext = file_ext[1:].lower()

                if file_ext == 'json':
                    self.__load_from_json()
                elif file_ext == 'csv':
                    self.__load_from_csv()
                else:
                    with open(self.file_path, 'r', encoding='utf-8', errors='replace') as file:
                        lines = [line.strip() for line in file.readlines()]
                        self.data = lines
            else:
                raise ValueError("File path must be provided.")

        except Exception as e:
            print(f"Error during load_from_file: {e}")

    # Returns json object CHORE: handle json list and json dict objects separately
    def to_json(self, indent=None):
        if self.data is None:
            self.__load_from_file()
        return json.dumps(self.data, indent=indent)

    # Sets data from a file or string
    def load_data(self, file_path=None, json_string=None):
        try:
            if file_path:
                self.file_path = file_path
            if self.file_path:
                self.__load_from_file()
            elif json_string:
                self.data = json.loads(json_string)
            else:
                raise ValueError("File path or JSON string must be provided.")
        except Exception as e:
            print(f"Error during from_json: {e}")
