# Insurance ERP - Deployment Guide

## Production Deployment Instructions

---

## Pre-Deployment Checklist

### Security
- [ ] Change `SECRET_KEY` in settings.py
- [ ] Set `DEBUG = False`
- [ ] Update `ALLOWED_HOSTS` with actual domain
- [ ] Configure `CSRF_TRUSTED_ORIGINS`
- [ ] Set up HTTPS/SSL certificate
- [ ] Configure secure cookies
- [ ] Update password hashing

### Database
- [ ] Set up PostgreSQL database
- [ ] Create database and user
- [ ] Test database connection
- [ ] Configure backup strategy
- [ ] Run migrations on production

### Storage
- [ ] Configure static files storage
- [ ] Set up media files storage (S3/Cloud)
- [ ] Configure CDN if needed

### Email
- [ ] Configure email backend
- [ ] Set up SMTP credentials
- [ ] Test email sending

### Monitoring
- [ ] Set up error tracking (Sentry)
- [ ] Configure logging
- [ ] Set up uptime monitoring
- [ ] Configure alerts

---

## Deployment Methods

### Option 1: Using Gunicorn + Nginx

#### Step 1: Install Gunicorn
```bash
pip install gunicorn
```

#### Step 2: Test Gunicorn
```bash
gunicorn insurance_erp.wsgi:application --bind 0.0.0.0:8000
```

#### Step 3: Create Systemd Service File
Create `/etc/systemd/system/insurance-erp.service`:

```ini
[Unit]
Description=Insurance ERP Gunicorn Application
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/insurance_erp
Environment="PATH=/path/to/insurance_erp/venv/bin"
ExecStart=/path/to/insurance_erp/venv/bin/gunicorn \
    --workers 4 \
    --worker-class sync \
    --bind unix:/path/to/insurance_erp/gunicorn.sock \
    insurance_erp.wsgi:application

[Install]
WantedBy=multi-user.target
```

#### Step 4: Enable Service
```bash
sudo systemctl daemon-reload
sudo systemctl enable insurance-erp
sudo systemctl start insurance-erp
```

#### Step 5: Configure Nginx
Create `/etc/nginx/sites-available/insurance-erp`:

```nginx
upstream insurance_erp {
    server unix:/path/to/insurance_erp/gunicorn.sock fail_timeout=0;
}

server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    # Redirect HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    # SSL Certificate
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    # SSL Configuration
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    client_max_body_size 20M;

    location /static/ {
        alias /path/to/insurance_erp/staticfiles/;
    }

    location /media/ {
        alias /path/to/insurance_erp/media/;
    }

    location / {
        proxy_pass http://insurance_erp;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

#### Step 6: Enable Nginx Site
```bash
sudo ln -s /etc/nginx/sites-available/insurance-erp /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

---

### Option 2: Using Docker

#### Dockerfile
```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Run gunicorn
CMD ["gunicorn", "insurance_erp.wsgi:application", "--bind", "0.0.0.0:8000"]
```

#### Docker Compose
```yaml
version: '3.8'

services:
  db:
    image: postgres:14
    environment:
      POSTGRES_DB: insurance_erp
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: secure_password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  web:
    build: .
    command: gunicorn insurance_erp.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      DATABASE_URL: postgresql://postgres:secure_password@db:5432/insurance_erp

  nginx:
    image: nginx:latest
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./staticfiles:/app/staticfiles
      - ./media:/app/media
    depends_on:
      - web

volumes:
  postgres_data:
```

#### Build and Run
```bash
docker-compose build
docker-compose up -d
```

---

### Option 3: Using Heroku

#### Step 1: Install Heroku CLI
```bash
curl https://cli.heroku.com/install.sh | sh
```

#### Step 2: Create Procfile
```
web: gunicorn insurance_erp.wsgi:application
release: python manage.py migrate
```

#### Step 3: Create Runtime.txt
```
python-3.10.0
```

#### Step 4: Deploy
```bash
heroku login
heroku create insurance-erp
git push heroku main
heroku addons:create heroku-postgresql:hobby-dev
heroku config:set SECRET_KEY="your-secret-key"
heroku run python manage.py migrate
heroku open
```

---

### Option 4: Using AWS EC2

#### Step 1: Launch EC2 Instance
- AMI: Ubuntu 20.04 LTS
- Instance Type: t3.micro (or larger)
- Security Groups: SSH (22), HTTP (80), HTTPS (443)

#### Step 2: SSH into Instance
```bash
ssh -i your-key.pem ubuntu@your-instance-ip
```

#### Step 3: Install Dependencies
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv nginx postgresql postgresql-contrib

# Create directory
mkdir /app
cd /app

# Clone repository
git clone https://github.com/kakkarot23/Insurance-ERP.git
cd Insurance-ERP/insurance_erp
```

#### Step 4: Set Up Python Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```

#### Step 5: Configure Database
```bash
sudo -u postgres psql
CREATE DATABASE insurance_erp;
CREATE USER insurance_user WITH PASSWORD 'strong_password';
GRANT ALL PRIVILEGES ON DATABASE insurance_erp TO insurance_user;
\q
```

#### Step 6: Update Django Settings
Update `insurance_erp/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'insurance_erp',
        'USER': 'insurance_user',
        'PASSWORD': 'strong_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = ['your-domain.com', 'your-instance-ip']
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

#### Step 7: Run Migrations
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

#### Step 8: Follow Gunicorn + Nginx setup above

---

## Environment Variables

Create `.env` file:

```env
# Django Settings
DEBUG=False
SECRET_KEY=your-very-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/insurance_erp

# Email
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# AWS S3 (Optional)
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_STORAGE_BUCKET_NAME=your-bucket

# Sentry (Optional)
SENTRY_DSN=your-sentry-dsn
```

---

## Database Migration to PostgreSQL

```bash
# Install PostgreSQL driver
pip install psycopg2-binary

# Update settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'insurance_erp',
        'USER': 'insurance_user',
        'PASSWORD': 'strong_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Dump SQLite data
python manage.py dumpdata > data.json

# Apply migrations to PostgreSQL
python manage.py migrate

# Load data
python manage.py loaddata data.json
```

---

## Monitoring & Logging

### Setup Sentry
```bash
pip install sentry-sdk

# In settings.py
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="your-sentry-dsn",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=False
)
```

### Configure Logging
```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/insurance-erp/django.log',
            'maxBytes': 1024 * 1024 * 10,  # 10MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['file', 'console'],
        'level': 'INFO',
    },
}
```

---

## Backup Strategy

### Daily Database Backup
```bash
# backup.sh
#!/bin/bash
BACKUP_DIR="/backups/insurance-erp"
DATE=$(date +%Y-%m-%d_%H-%M-%S)

pg_dump insurance_erp | gzip > $BACKUP_DIR/insurance_erp_$DATE.sql.gz

# Keep only last 7 days
find $BACKUP_DIR -name "insurance_erp_*.sql.gz" -mtime +7 -delete
```

### Automated Backup (Cron)
```bash
0 2 * * * /path/to/backup.sh  # Daily at 2 AM
```

---

## Performance Optimization

### Database Connection Pooling
```bash
pip install django-db-pool
```

### Caching
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

### Static Files CDN
```python
# Use AWS CloudFront or similar
STATIC_URL = 'https://cdn.yourdomain.com/static/'
```

---

## SSL/TLS Certificate

### Using Let's Encrypt
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot certonly --nginx -d yourdomain.com
sudo certbot renew --dry-run  # Test renewal
```

---

## Post-Deployment

### Verification Steps
```bash
# Check application status
curl https://yourdomain.com

# Check database
python manage.py dbshell

# Check migrations
python manage.py showmigrations

# Test email
python manage.py shell
from django.core.mail import send_mail
send_mail('Test', 'Test message', 'from@example.com', ['to@example.com'])
```

---

## Troubleshooting

### Check Logs
```bash
# Nginx
sudo tail -f /var/log/nginx/error.log

# Gunicorn (Systemd)
sudo journalctl -u insurance-erp -f

# Application
tail -f /var/log/insurance-erp/django.log
```

### Common Issues
```bash
# Permission denied
sudo chown -R www-data:www-data /path/to/insurance_erp

# Port already in use
sudo lsof -i :8000
sudo kill -9 <PID>

# Database connection error
python manage.py dbshell
```

---

## Scaling Checklist

- [ ] Load testing completed
- [ ] Database optimized and indexed
- [ ] Static files on CDN
- [ ] Caching implemented
- [ ] Multiple Gunicorn workers
- [ ] Load balancer configured
- [ ] Monitoring alerts set up
- [ ] Backup system tested
- [ ] Disaster recovery plan

---

## Support Resources

- Django Deployment: https://docs.djangoproject.com/en/4.2/howto/deployment/
- Gunicorn: https://gunicorn.org/
- Nginx: https://nginx.org/
- PostgreSQL: https://www.postgresql.org/docs/

---

**Last Updated:** December 2024
