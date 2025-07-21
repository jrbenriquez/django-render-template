# Django App Template

This is a minimalist Django project template designed for fast development and clear structure. It includes a modern frontend stack and comes with a basic setup to get started quickly.

---

## 🚀 Features

- Django backend with sensible defaults  
- Tailwind CSS for utility-first styling  
- Vanilla JavaScript for frontend interactivity  
- Clean project structure for easy customization  
- Poetry for dependency and environment management  

---

## 🧱 Tech Stack

- **Backend**: [Django](https://www.djangoproject.com/)  
- **Frontend**: [Tailwind CSS](https://tailwindcss.com/), Vanilla JS  
- **Package Management**: [Poetry](https://python-poetry.org/)  
- **Design Inspiration**: [HyperUI](https://www.hyperui.dev/) components (optional)

---

## ⚙️ Quick Setup Guide

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### 2. Install Dependencies
Ensure [Poetry](https://python-poetry.org/) is installed:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Then install project dependencies:
```bash
poetry install
```

### 3. Apply Migrations
```bash
poetry run python manage.py migrate
```

### 4. Create a Superuser
```bash
poetry run python manage.py createsuperuser
```

### 5. Run the Development Server
```bash
poetry run python manage.py runserver
```

Now open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## 🛠️ Common Commands

### Collect Static Files
```bash
poetry run python manage.py collectstatic
```

### Load Fixture Data (if applicable)
```bash
poetry run python manage.py loaddata <fixture-file>
```

---

This template is intended to be a clean foundation for building Django apps of any kind. You can extend it with additional packages, apps, and frontend tooling as needed.
