import os
import argparse

from report_names import REPORT_NAMES

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--files', required=True, nargs='+', help='Path to CSV files')
    parser.add_argument(
        '--report', required=True, help='Report name')
    args = parser.parse_args()
    validate_files_exist(args.files, parser)
    validate_report_name(args.report, parser)
    return args

def validate_files_exist(files_paths, parser):
    for file_path in files_paths:
        if not os.path.exists(file_path):
            parser.error(f'File "{file_path}" does not exist')

def validate_report_name(report_name, parser):
    if report_name not in REPORT_NAMES:
        parser.error(
                    f'Report "{report_name}" does not exist. '
                    f'Available reports: {REPORT_NAMES}'
                )
