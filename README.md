# ZeroBadger

**ZeroBadger** is a minimalist budgeting tool built around the concept of **Zero-Based Budgeting (ZBB)** — a proven strategy that gives every peso a purpose.

## 💸 What is Zero-Based Budgeting?

Zero-Based Budgeting means assigning **every peso of your income** to a specific job — whether that's an expense, savings, or a financial goal. By the end of each budgeting cycle, your income minus expenses should equal **₱0**, ensuring that all money is accounted for with intention.

Rather than leaving “leftover” money untracked, ZeroBadger helps users clearly see where every peso goes and encourages better financial awareness.

## 🛠 What ZeroBadger Offers

- Clean, distraction-free interface
- Dual budgeting and spending views (budget-first or simple expense tracking)
- Gamified nudges to help users fully allocate their income
- Summary breakdown of available funds
- Support for both beginners and detailed budgeters

Whether you're just trying to stay on top of spending, or proactively planning every detail of your budget — ZeroBadger makes it approachable and intuitive.

## 🐍 Tech Stack

- **Backend**: Django
- **Frontend**: Tailwind CSS, Vanilla JS
- **Design System**: Inspired by HyperUI

---

> ZeroBadger is built with simplicity and clarity in mind — so budgeting becomes a habit, not a chore.

## Quick Setup Guide

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd <your-project-folder>
```

### 2. Install Dependencies
Ensure **Poetry** is installed. If not, install it first:
```sh
curl -sSL https://install.python-poetry.org | python3 -
```
Then install project dependencies:
```sh
poetry install
```

### 3. Apply Migrations
```sh
poetry run python manage.py migrate
```

### 4. Create a Superuser
```sh
poetry run python manage.py createsuperuser
```

### 5. Run the Development Server
```sh
poetry run python manage.py runserver
```
Now, visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Additional Commands

### Collect Static Files
```sh
poetry run python manage.py collectstatic
```

### Load Sample Data (if available)
```sh
poetry run python manage.py loaddata <fixture-file>
```
