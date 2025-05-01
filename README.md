# Market Price Finder

A Django-based web application that helps users compare product prices across different markets.

## Features

- Product price comparison across multiple markets
- Search and filter products by category and market
- Sort products by price, name, and rating
- Highlight cheapest prices
- User-friendly interface with responsive design

## Prerequisites

- Python 3.8 or higher
- PostgreSQL (for production)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/berkan-ridvan/market-price-finder.git
cd market-price-finder
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with the following variables:
```env
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
DATABASE_URL=postgres://user:password@localhost:5432/dbname
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

## Development

To run the development server:
```bash
python manage.py runserver
```

## Production Deployment

### Heroku Deployment

1. Install Heroku CLI and login:
```bash
heroku login
```

2. Create a new Heroku app:
```bash
heroku create your-app-name
```

3. Add PostgreSQL addon:
```bash
heroku addons:create heroku-postgresql:hobby-dev
```

4. Set environment variables:
```bash
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-secret-key-here
heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
```

5. Deploy to Heroku:
```bash
git push heroku main
```

6. Run migrations:
```bash
heroku run python manage.py migrate
```

7. Create superuser:
```bash
heroku run python manage.py createsuperuser
```

### Other Platforms

For other platforms (DigitalOcean, AWS, etc.), follow these general steps:

1. Set up a PostgreSQL database
2. Configure your web server (Nginx, Apache)
3. Set up a WSGI server (Gunicorn)
4. Configure environment variables
5. Run migrations and create superuser
6. Collect static files:
```bash
python manage.py collectstatic --noinput
```

## Security Considerations

- Keep your SECRET_KEY secure
- Use HTTPS in production
- Regularly update dependencies
- Monitor Django security releases
- Implement proper user authentication
- Use environment variables for sensitive data

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
