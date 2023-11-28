import sys
import os
from tools.excel_handler.excel_worker import ExcelSheetWorker

def extract_excel():
    # Usage
    if len(sys.argv) != 2:
        print("Usage python main.py <file>")
        sys.exit(1)
    file_path = sys.argv[1]

    ExcelSheetWorker.excel_to_json(file_path)
    


if __name__ == "__main__":
#    extract_excel()
