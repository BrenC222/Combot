import pandas as pd
import json
import os

class ExcelSheetWorker:
    def __init__(self, sheet_name, sheet_data):
        self.sheet_name = sheet_name
        self.sheet_data = sheet_data
        
    def to_json(self):
        return {self.sheet_name: self.sheet_data}

    def _save_to_json_file(self, file_path, indent=2):
        with open(file_path, 'w', encoding='utf-8', errors='replace') as file:
            json.dump(self.to_json(), file, indent=indent)

    @staticmethod
    def _get_sheet_names(excel_file_path):
        try:
            with pd.ExcelFile(excel_file_path) as excel_file:
                sheet_names = [sheet_name for sheet_name in excel_file.sheet_names]
            return sheet_names
        except Exception as e:
            print(f"Error reading excel file: {e}")
            return []

    @staticmethod
    def _process_frame_sheet(excel_file_path, sheet_name):
        df = pd.read_excel(excel_file_path, sheet_name, skiprows=1)
        sheet_data = df.to_dict(orient='records')
        return sheet_data

    @staticmethod
    def _process_meta_sheet(excel_file_path, sheet_name):
        df = pd.read_excel(excel_file_path, sheet_name)
        sheet_data = df.to_dict(orient='records')
        return sheet_data
        
    @classmethod
    def excel_to_json(cls, file_path):
        tsheet_name = cls._get_sheet_names(file_path)
        tsheet_data = {}
        for sheet_name in tsheet_name:
            print(f"Working on {sheet_name}")
            if sheet_name.endswith('-meta'):
                sheet_data = cls._process_meta_sheet(file_path, sheet_name)
                tsheet_data[sheet_name] = cls(sheet_name, sheet_data)
            else:
                sheet_data = cls._process_frame_sheet(file_path, sheet_name)
                tsheet_data[sheet_name] = cls(sheet_name, sheet_data)
                
            print("Done...")
            
        for sheet_name, sheet_data in tsheet_data.items():
            if sheet_name.endswith('-meta'):
                output_path = f"data/meta/{sheet_name}_output.json"
                print(f"Writing file {output_path}")
                sheet_data._save_to_json_file(output_path)
            else:
                output_path = f"data/frame/{sheet_name}_output.json"
                print(f"Writing file {output_path}")
                sheet_data._save_to_json_file(output_path)

            print("Done...")
