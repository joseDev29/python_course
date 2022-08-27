import os
import re
import math
from pathlib import Path
from datetime import date
from time import time


def format_result(filename: str, serie_number: str) -> str:
    return "{:<15}   {:<8}".format(filename, serie_number)


def main():
    files_path = Path(Path.cwd(), 'files_dir')

    current_date = date.today().strftime('%Y/%m/%d')

    print(f"Search date: {current_date}\n")

    series_numbers_count = 0
    series_numbers_pattern = r'N\D{3}-\d{5}'

    init_time = time()

    print(format_result('FILE', 'SERIE NUMBER'))
    print(format_result('----', '------------'))

    for fold, sub_fold, files in os.walk(files_path):
        for filename in files:
            file_path = Path(fold, filename)
            file = open(file_path)
            file_content = file.read()
            file.close()
            match_result = re.findall(series_numbers_pattern, file_content)

            for matched in match_result:
                series_numbers_count += 1
                print(format_result(filename, matched))

    end_time = time()

    print(f"\nSearch results: {series_numbers_count}")

    search_duration = math.ceil(end_time - init_time)
    print(f"\nSearch duration: {search_duration} seconds")


main()
