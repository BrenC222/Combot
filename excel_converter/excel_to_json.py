import pandas as pd
import json
import os

class ExcelSheetWorker:
    def __init__(self, excel_file_path, sheet_name):
        self.df = pd.read_excel(excel_file_path, sheet_name, skiprows=1)
        self.sheet_name = sheet_name

    def to_json(self):
        json_data = self.df.to_dict(orient='records')
        return json_data

    @classmethod
    def get_sheet_names(cls, excel_file_path):
        # Open excel file and get the sheet names (ie Character names)
        excel_file = pd.ExcelFile(excel_file_path)
        sheet_names = [sheet_name for sheet_name in excel_file.sheet_names if not sheet_name.endswith('-meta')]
        excel_file.close()
        return sheet_names

    def save_to_json_file(self, file_path, indent=2):
        with open(file_path, 'w') as file:
            json.dump(self.to_json(), file, indent=indent)
