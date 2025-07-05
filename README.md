# Django Blog Project

A minimal yet functional blog application built with Django.  
Supports Persian (Farsi) UI and includes essential features like user authentication, tagging, and comments.

---

## 🚀 Features

- User registration & login
- Create, edit, and delete blog posts
- Tagging system for organizing content
- Comment section for each post
- Bilingual support (mainly Persian 🇮🇷)

---

## ⚙️ Installation

1. **Clone the repository**  
```bash
https://github.com/sepy-dev/My-Blog-Django.git
cd My-Blog-Django

    Install dependencies

pip install -r requirements.txt

    Run migrations

python manage.py migrate

    Start the development server

python manage.py runserver

Now open http://localhost:8000 in your browser.
🧾 Requirements

    Python 3.8+

    Django 4.x

    django-taggit

    Other optional dependencies may include python-decouple, django-crispy-forms, etc.

📁 Project Structure

blog_project/
├── blog/                 # Main blog app
├── blog_project/         # Project settings
├── templates/            # HTML templates (mostly in Persian)
├── static/               # CSS/JS assets
├── media/                # Uploaded files
├── manage.py
└── requirements.txt

👤 Author

Sepehr Ramzany
📧 Email: sepehr.ramzany@gmail.com
🐙 GitHub: sepy-dev
🐦 Twitter (X): @sepy_dev
📷 Instagram: @sepehr.ramzany
📄 License

This project is licensed under the MIT License.

    Made with ❤️ in Iran. UI is primarily in Persian
