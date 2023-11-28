import pandas as pd
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

    def excel_convert(file_path):
        fighter_names = ExcelSheetWorker.get_sheet_names(file_path)
        fighter_infos = {}
        for fighter_name in fighter_names:
            print(fWorking on {fighter_name})
            fighter_infos[fighter_name] = ExcelSheetWorker(file_path, fighter_name)
            print(Done...)
            
        for fighter_name, info in fighter_infos.items():
            file_path = fdata/frame/{fighter_name}_output.json
            print(fWriting file {file_path})
            info.save_to_json_file(file_path)
            print(Done...)
