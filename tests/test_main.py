import sys
import pytest

from main import main

def test_main(monkeypatch, tmp_path, capsys):
    file = tmp_path / 'file.csv'
    file.write_text(
        'name,position,completed_tasks,performance,skills,team,'
        'experience_years\n'
        'Вася Пупкин,Backend,10,3,Python,API Team,0\n'
        'Иван Иваныч,Backend,30,5,Python,API Team,100\n'
        'Марья Ивановна,Frontend,20,5,JS,Web Team, 10'
        )
    monkeypatch.setattr(
        sys,
        'argv',
        ['main.py', '--files', str(file), '--report', 'performance']
    )
    main()
    captured = capsys.readouterr()

    assert 'Backend' in captured.out
    assert '4' in captured.out
    assert 'Frontend' in captured.out
    assert '5' in captured.out


def test_main_without_files_arguments(monkeypatch):
    monkeypatch.setattr(
        sys,
        'argv',
        ['main.py', '--report', 'performance']
    )
    with pytest.raises(SystemExit):
        main()



def test_main_without_report_arguments(monkeypatch, tmp_path):
    file = tmp_path / 'file.csv'
    monkeypatch.setattr(
        sys,
        'argv',
        ['main.py', '--files', str(file)]
    )
    with pytest.raises(SystemExit):
        main()


def test_main_with_wrong_report(monkeypatch, tmp_path):
    file = tmp_path / 'file.csv'
    monkeypatch.setattr(
        sys,
        'argv',
        ['main.py', '--files', str(file), '--report', 'ололо']
    )
    with pytest.raises(SystemExit):
        main()
