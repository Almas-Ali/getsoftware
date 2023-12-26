# Getsoftware - A Django practice project

First commited: `Sat Jun 19 16:55:21 2021 +0600`

Not actively maintained. Just a practice project. If you want to use it, you can.

How much bad my code was back in those days. I'm not even going to fix it. Just going to leave it as it is. For some security reasons, I have removed all previous commits in this public repo.

## Features

- User can register and login
- Admin can add software
- Admin can add category
- User can search software
- Suggestions are shown when user search
- User can download software
- User can comment on software after login
- User can reply to comments after login
- Download count is shown
- User can search software
- User can see software by category
- Modern UI
- Responsive

## Installation

```bash
# Clone the repo
git clone https://github.com/Almas-Ali/getsoftware && cd getsoftware

# Create virtual environment
python -m venv venv

# Activate virtual environment (Linux and Mac)
source venv/bin/activate

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (optional for admin panel)
# Only need when you want to add any software or category
python manage.py createsuperuser

# Run server
python manage.py runserver

```

Open http://127.0.0.1:8000 in your browser to see the app.

## Screenshots

### Home page

![Home](screenshots/01_home_page.png)

### Software page

![Software](screenshots/02_software_page.png)

### Contact page

![Contact](screenshots/03_contact_page.png)

### Category page

![Category](screenshots/04_category_page.png)

### Search page

![Search](screenshots/05_search_page.png)

### Register page

![Register](screenshots/06_register_page.png)

### Login page

![Login](screenshots/07_login_page.png)

### Search page

![Search](screenshots/08_search_page.png)

### Newsletter page

![Newsletter](screenshots/09_newsletter_page.png)

## License

[MIT](LICENSE)
