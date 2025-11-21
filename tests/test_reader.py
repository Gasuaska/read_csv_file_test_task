from reader import read_csv, average_performance, sorted_stats

def test_read_empty_csv(tmp_path):
    file = tmp_path / 'file.csv'
    file.write_text(
        'name,position,completed_tasks,performance,skills,team,'
        'experience_years\n'
    )
    result = read_csv([file])
    assert result == {}

def test_read_single_csv(tmp_path):
    file = tmp_path / 'file.csv'
    file.write_text(
        'name,position,completed_tasks,performance,skills,team,'
        'experience_years\n'
        'Вася Пупкин,Backend,10,3,Python,API Team,0\n'
        'Иван Иваныч,Backend,30,5,Python,API Team,100'
        )
    result= read_csv([file])
    assert result['Backend']['total_perf'] == 8.0
    assert result['Backend']['count'] == 2


def test_read_multiple_csv(tmp_path):
    file1 = tmp_path / 'file1.csv'
    file1.write_text(
        'name,position,completed_tasks,performance,skills,team,'
        'experience_years\n'
        'Вася Пупкин,Backend,10,3,Python,API Team,0'
        )
    file2 = tmp_path / 'file2.csv'
    file2.write_text(
        'name,position,completed_tasks,performance,skills,team,'
        'experience_years\n'
        'Иван Иваныч,Backend,30,5,Python,API Team,100'
        )
    result= read_csv([file1, file2])
    assert result['Backend']['total_perf'] == 8.0
    assert result['Backend']['count'] == 2


def test_average_performance_empty():
    assert average_performance({}) == []


def test_average_performance():
    stats = {
        'Backend': {'total_perf': 9.4, 'count': 2},
        'Frontend': {'total_perf': 4.7, 'count': 1},
    }
    result = average_performance(stats)
    average_stats = [
        ('Backend', 4.7),
        ('Frontend', 4.7)
    ]
    assert result == average_stats


def test_sorted_stats():
    stats = [
        ('Frontend', 2),
        ('Backend', 5),
    ]
    result = sorted_stats(stats)
    presorted_stats =[
        ('Backend', 5),
        ('Frontend', 2),
    ]
    assert result == presorted_stats