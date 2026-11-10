# Django Staff Filter App

A Django learning project focused on querying, filtering, and aggregating employee data using the Django ORM.

## Features

- Display all employees with their names, departments, and salaries.
- Filter employees earning more than €3,000 per month.
- Count employees earning at least €5,000 per month.
- Calculate the average salary in the Sales department.
- Display employees hired before January 1, 2022, excluding the HR department.

## Technologies

- Python
- Django
- SQLite
- HTML
- Django Template Language
- Git and GitHub

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Qualle1980/Django_Staff_Filter_App.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Django_Staff_Filter_App
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment on Windows:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Populate the database with sample employees:

   ```bash
   python manage.py shell < populate.py
   ```

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

Open the following URL in your browser:

http://127.0.0.1:8000/employees/

The application displays employee information and the results of the five Django ORM exercises.

## Django ORM Concepts

This project demonstrates:

- `all()` for retrieving records
- `filter()` for conditional queries
- `exclude()` for excluding records
- `count()` for counting records
- `aggregate()` and `Avg()` for calculating averages
- ForeignKey relationships
- Date-based filtering
- Passing QuerySets from views to templates

## Project Status

All five exercises have been completed and the Django system check passes without errors.

## Author

GitHub: [Qualle1980](https://github.com/Qualle1980)

## Acknowledgements

Based on a training exercise provided by Developer Akademie.