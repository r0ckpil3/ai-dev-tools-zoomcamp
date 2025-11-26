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
   ```bash
   git clone <repository-url>
   cd django-todo
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtualenv

   - bash / zsh / sh:
     ```bash
     source venv/bin/activate
     ```

   - fish (you can either use the venv python directly, or run under bash):
     ```fish
     # Option 1: use python from the venv without activating
     ./venv/bin/python -m pip install -r requirements.txt

     # Option 2: activate under bash if you prefer activation
     bash -lc "source venv/bin/activate && pip install -r requirements.txt"
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Apply migrations:
   ```
   python manage.py migrate
   ```

2. Run the development server:
   ```bash
   # Use the venv python to avoid activation headaches
   ./venv/bin/python manage.py runserver
   ```

3. Open your browser and go to `http://127.0.0.1:8000/` (todo list) or
   `http://127.0.0.1:8000/home/` (home page).

## Usage

- You can add new todo items, view existing ones, edit them, and delete them as needed.

## Tests

Run tests with the venv python:

```bash
./venv/bin/python manage.py test
```

## Create admin user (non-interactive example)

```bash
./venv/bin/python manage.py createsuperuser --username admin --email admin@example.com --noinput
# then set password in a shell (or use a management command) or create interactively
```

Or create a superuser interactively:

```bash
./venv/bin/python manage.py createsuperuser
```

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.