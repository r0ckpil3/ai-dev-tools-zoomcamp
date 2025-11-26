# Django Todo Application

This is a simple Todo application built with Django. It allows users to create, read, update, and delete todo items.

## Project Structure

```
django-todo/
├── manage.py
├── requirements.txt
├── .gitignore
├── todo_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── todo/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── tests.py
    ├── migrations/
    │   └── __init__.py
    ├── templates/
    │   └── todo/
    │       └── todo_list.html
    └── static/
        └── todo/
            └── css/
                └── styles.css
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd django-todo
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Apply migrations:
   ```
   python manage.py migrate
   ```

2. Run the development server:
   ```
   python manage.py runserver
   ```

3. Open your browser and go to `http://127.0.0.1:8000/` to view the application.

## Usage

- You can add new todo items, view existing ones, edit them, and delete them as needed.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.