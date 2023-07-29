<h1 align="center">Todo App</h1>

<p align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python Logo" width="150" height="150">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg" alt="Django Logo" width="150" height="150">
</p>

## 📝 Project Overview

Todo App is a web application built with Django that allows users to create, modify, and delete their todos. It provides a simple and intuitive interface for managing tasks efficiently. The app is designed with a clean and modern look, along with icons for an enhanced user experience.

## ✨ Features

- **User Authentication:** Users can sign up, log in, and log out to access their personal todo lists securely.
- **Create Todo:** Add new tasks to your todo list with a title, description, and optional due date.
- **Update Todo:** Modify existing todos by editing their title, description, or due date.
- **Delete Todo:** Remove completed or unnecessary tasks from your list effortlessly.
- **Responsive Design:** The app is mobile-friendly, ensuring seamless usage on various devices.

## 🛠️ Specifications

- Python version: 3.9.7
- Django version: 3.2.8
- Database: SQLite (default), but can be configured for other databases.
- External libraries used:
  - Bootstrap 5 (for styling and layout)
  - Font Awesome (for icons)
  - jQuery (for interactivity)

## 🚀 Setup

Follow these steps to set up the Todo App locally:

1. Clone the repository:

git clone https://github.com/yourusername/todo-app.git

2. Create a virtual environment (optional but recommended):

python3 -m venv venv

3. Activate the virtual environment:

- Windows (Command Prompt):

  ```
  venv\Scripts\activate
  ```

- macOS and Linux:

  ```
  source venv/bin/activate
  ```

4. Install the required dependencies:

pip install -r requirements.txt

5. Run database migrations:

python manage.py migrate

6. Create a superuser to access the Django admin panel:

python manage.py createsuperuser

7. Start the development server:

python manage.py runserver

8. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the Todo App.

## 🙏 Acknowledgments

- The Todo App was developed with the help of the Django web framework and various open-source libraries and icons, which greatly contributed to its functionality and aesthetics.
