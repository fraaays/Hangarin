# Hangarin

Hangarin is a web-based To-Do and planner application built using Django. It helps users organize tasks, manage notes, and categorize activities efficiently.

## Link for Demonstration
https://fraaays.pythonanywhere.com

## Features

* Task and note management
* Category-based organization
* Dashboard overview
* User authentication (Google login using Django Allauth)
* Create, update, and delete notes

## Technologies Used

* Django (Python)
* HTML, CSS, Bootstrap
* SQLite
* Django Allauth

## Installation

1. Clone the repository
2. Navigate to the project folder
3. Create a virtual environment

```
python -m venv venv
venv\Scripts\activate
```

4. Install dependencies

```
pip install -r requirements.txt
```

5. Run migrations

```
python manage.py migrate
```

6. Create superuser

```
python manage.py createsuperuser
```

7. Run the server

```
python manage.py runserver
```

## Usage

* Open browser and go to `http://127.0.0.1:8000/`
* Login using your account or Google
* Start creating tasks and categories

## Project Structure

* `planner/` - main app (tasks, notes, categories)
* `templates/` - HTML files
* `manage.py` - Django command tool

## Author

Frilyn Alicos

GitHub: https://github.com/fraaays

## License

This project is for educational purposes only.
