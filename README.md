# Система знижок для постійних клієнтів

Навчальний проєкт до практичного заняття з міграцій Django. Створений на основі
шаблону курсу `web-programming-2026-template`.

## Що вже є

- Застосунок `cards` з моделлю `DiscountCard` (`cards/models.py`).
- Автоматично згенерована міграція `cards/migrations/0001_initial.py`.
- Модель зареєстрована в адмінці (`cards/admin.py`), щоб зручно переглядати дані.

Таблиця моделі в базі називається `cards_discountcard`.

## Корисні команди для заняття

```bash
python manage.py showmigrations cards                         # які міграції застосовані
python manage.py sqlmigrate cards 0001                        # який SQL виконує міграція
python manage.py makemigrations cards --empty --name <назва>  # порожня міграція
python manage.py migrate cards <номер>                        # перейти до конкретної міграції
python manage.py shell                                        # інтерактивна консоль
```

## Local setup

Requires the latest patch release of Python 3.12, 3.13, or 3.14. Run these commands from the project directory containing
`manage.py`.

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   
   # for linux/macos
   source .venv/bin/activate
   # for Windows:
   .venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   python -m pip install -r requirements-dev.txt
   ```


3. Apply migrations to create the local SQLite database:

   ```bash
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Endpoints

With the server running at `http://127.0.0.1:8000`:

| URL | Behavior |
| --- | --- |
| http://127.0.0.1:8000/ | No application homepage; may show Django's development welcome page while `DEBUG = True` |
| http://127.0.0.1:8000/admin/ | Django admin, available after applying migrations |

With `DEBUG = False`, unmatched URLs such as `/` return HTTP 404.

To create an account for admin login, run this after applying migrations:

```bash
python manage.py createsuperuser
```

## Git attributes

Git detects text files automatically and normalizes them to LF. Checkouts use
LF on Linux and Windows, while `.bat` and `.cmd` files use CRLF. Binary files
are auto-detected and left unchanged, helping avoid newline-only diffs.


## Code style and submission verification

All submissions are required to adhere to PEP-8, Django best practices, and standard HTML/CSS/JS formatting. A deterministic cross-platform utility is provided to help you check and format your code.

### 1. Verification (Check Mode)
Before submitting, verify that all files adhere to the required standards:

```bash
python check_submission.py
```

If all checks pass, you are ready to submit! If any checks fail, review the error output or run the auto-formatter below.

### 2. Auto-Formatting
To automatically format Python files, fix safe PEP-8 rules, format Django HTML templates, and format CSS/JS static files:

```bash
python check_submission.py --format
```

### 3. PyCharm Integration
If you use PyCharm:
- **One-Click Run:** In the top-right toolbar run configurations dropdown, select **"Verify Submission"** or **"Format Project"** and click the green **Play** button.

## Development only

The included settings use `DEBUG = True`, a development secret key, and a local
SQLite database. The default mailer uses the console backend: email is printed
to the process's console instead of being delivered.

This configuration and Django's development server are not suitable for
production deployment.
