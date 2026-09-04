# Vereshchagin Museum

Full-stack web application developed for the V. V. Vereshchagin Museum.

The project provides access to paintings, biographical materials and textual content related to Vasily Vereshchagin and his family. It also includes restricted content available only to authorized users.

## Features

- Catalogue of artworks
- Biographical and textual materials
- Public and restricted content
- User authentication
- Role-based access to protected materials
- Administrative interface for content management
- Image and media handling
- REST API for communication between frontend and backend
- Responsive web interface

## Tech Stack

### Frontend

- Vue 3
- Nuxt 3
- JavaScript
- Axios
- Vuetify
- SCSS
- Swiper
- Nuxt Image

### Backend

- Python
- Django
- Django REST Framework
- django-filter
- drf-yasg / Swagger
- Pillow
- SQLite for local development

## Backend Setup

Create and activate a virtual environment:

python -m venv venv

Linux / macOS:

source venv/bin/activate

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r req.txt

Run migrations:

cd code/backend
python manage.py migrate

Start the backend:

python manage.py runserver

## Frontend Setup

cd code/frontend
npm install
npm run dev

## Production

The project was prepared for deployment on an Ubuntu server using Docker.

The source code and deployment instructions were delivered to the customer after development.

## About

Commercial project developed as a full-stack application for a museum information system.

The repository is published as part of my development portfolio.
