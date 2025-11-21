from tabulate import tabulate

from cli import parse_arguments, validate_files_exist, validate_report_name
from reader import read_csv, average_performance, sorted_stats

def main():
    args = parse_arguments()
    stats = read_csv(args.files)
    avg = average_performance(stats)
    sorted = sorted_stats(avg)
    print(tabulate(
        sorted,
        headers=['Position', 'Performance'],
        tablefmt='simple'
        ))

    

if __name__ == '__main__':
    main()