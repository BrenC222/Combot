import sys
import os
from tools.excel_converter.excel_to_json import ExcelSheetWorker

def main():
    # Usage
    if len(sys.argv) != 2:
        print("Usage python main.py <file>")
        sys.exit(1)
    file_path = sys.argv[1]

#    excel_convert(file_path)
    


if __name__ == "__main__":
    main()
