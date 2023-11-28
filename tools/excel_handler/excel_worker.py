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

    def _get_sheet_names(excel_file_path):
        # Open excel file and get the sheet names (ie Character names)
        excel_file = pd.ExcelFile(excel_file_path)
        sheet_names = [sheet_name for sheet_name in excel_file.sheet_names if not sheet_name.endswith('-meta')]
        excel_file.close()
        return sheet_names

    def _save_to_json_file(self, file_path, indent=2):
        with open(file_path, 'w', encoding='utf-8', errors='replace') as file:
            json.dump(self.to_json(), file, indent=indent)

    @classmethod
    def excel_to_json(cls, file_path):
        sheet_names = cls._get_sheet_names(file_path)
        sheet_data = {}
        for sheet_name in sheet_names:
            print(f"Working on {sheet_name}")
            sheet_data[sheet_name] = cls(file_path, sheet_name)
            print("Done...")
            
        for sheet_name, data in sheet_data.items():
            file_path = f"data/frame/{sheet_name}_output.json"
            print(f"Writing file {file_path}")
            data._save_to_json_file(file_path)
            print("Done...")
