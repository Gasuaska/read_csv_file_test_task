import csv
import tabulate


def read_csv(file_names):
    stats = {}
    for file_name in file_names:
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                position = line['position']
                performance = float(line['performance'])
                if position in stats:
                    stats[position]['total_perf'] += performance
                    stats[position]['count'] += 1
                else:
                    stats[position] = {'total_perf': performance, 'count': 1}
    return stats


def average_performance(stats):
    average_stats = []
    for position, data in stats.items():
        avg = round(data['total_perf'] / data['count'], 2)
        average_stats.append((position, avg))
    return average_stats


def sorted_stats(average_stats):
    sorted_stats = sorted(average_stats, key=lambda x: x[1], reverse=True)
    return sorted_stats
