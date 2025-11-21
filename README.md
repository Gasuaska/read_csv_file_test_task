# read_csv_file_test_task

Скрипт для анализа эффективности работы разработчиков по CSV-файлам. Этот скрипт читает файлы и выводит среднее арифметическое столбца Performance.

## Установка

1. Клонируем репозиторий:
git clone (https://github.com/Gasuaska/read_csv_file_test_task.git)

cd read_csv_file_test_task

Создаём и активируем виртуальное окружение:

python -m venv venv

source venv/bin/activate  # Linux/macOS

venv\Scripts\activate     # Windows

Устанавливаем зависимости:

pip install -r requirements.txt

Использование

python main.py --files path/to/file1.csv path/to/file2.csv --report performance

--files — пути к CSV-файлам (можно несколько)


--report — имя отчёта (например, performance)

Запуск тестов:

pytest --cov=.

Используется pytest и pytest-cov

Покрытие основных функций: cli.py, reader.py и main.py
