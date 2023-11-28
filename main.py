import sys
import os
from json_helper.json_obj import JsonObj
from playable_character.fighter_obj import Fighter
from excel_converter.excel_to_json import ExcelSheetWorker
from discord_bot.bot_obj import Combot

def excel_convert(file_path):
    fighter_names = ExcelSheetWorker.get_sheet_names(file_path)
    fighter_infos = {}
    for fighter_name in fighter_names:
        print(f"Working on {fighter_name}")
        fighter_infos[fighter_name] = ExcelSheetWorker(file_path, fighter_name)
        print("Done...")
    for fighter_name, info in fighter_infos.items():
        file_path = f"data/frame/{fighter_name}_output.json"
        print(f"Writing file {file_path}")
        info.save_to_json_file(file_path)
        print("Done...")

def main():
    # Usage
    if len(sys.argv) != 2:
        print("Usage python main.py <file>")
        sys.exit(1)
    # Converts given file to json files
#    file_path = sys.argv[1]
#    excel_convert(file_path)
    


if __name__ == "__main__":
    main()
