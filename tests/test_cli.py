import sys
import pytest
from types import SimpleNamespace

from cli import parse_arguments, validate_files_exist, validate_report_name


def test_parse_arguments(monkeypatch, tmp_path):
    file = tmp_path / 'file.csv'
    file.write_text(
        'name,position,completed_tasks,performance,skills,team,'
        'experience_years\nВася Пупкин,Backend,10,3,Python,API Team,0'
        )
    monkeypatch.setattr(
        sys,
        'argv',
        ['main.py', '--files', str(file), '--report', 'performance']
    )
    args = parse_arguments()
    assert args.report == 'performance'
    assert args.files == [str(file)]


def test_parse_arguments_missing(monkeypatch):
    import sys
    monkeypatch.setattr(sys, 'argv', ['main.py'])
    import cli
    with pytest.raises(SystemExit):
        cli.parse_arguments()


def test_validate_files_doesnt_exist_error():
    parser = SimpleNamespace(
        error=lambda msg: (_ for _ in ()).throw(SystemExit(msg)))
    with pytest.raises(SystemExit):
        validate_files_exist(['ололо.csv'], parser)

def test_validate_report_name_error():
    parser = SimpleNamespace(
        error=lambda msg: (_ for _ in ()).throw(SystemExit(msg)))
    with pytest.raises(SystemExit):
        validate_report_name('Уволен', parser)
