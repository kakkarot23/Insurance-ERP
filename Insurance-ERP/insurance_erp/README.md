# Insurance ERP System

A comprehensive Python Django-based Enterprise Resource Planning (ERP) system for insurance companies.

## Features

### 1. **Policy Lifecycle Management**
   - Create and manage insurance policies
   - Track policy status (Draft, Active, Suspended, Expired, Cancelled)
   - Support for multiple policy types (Life, Health, Auto, Property, Marine)
   - Policy holder information and coverage details

### 2. **Premium Calculations**
   - Calculate premiums with adjustable risk factors
   - Apply taxes and discounts automatically
   - Generate detailed premium breakdown
   - Real-time calculation interface

### 3. **KYC Onboarding**
   - Know Your Customer verification process
   - Support for Individual, Corporate, and Partnership entities
   - Document upload and verification
   - Support for PAN, Aadhar, and other identity documents
   - Address verification and management

### 4. **Claims Processing**
   - File and track insurance claims
   - Multiple claim statuses (Filed, Under Review, Approved, Rejected, Paid)
   - Claim approval workflow with amount verification
   - Document attachment for claims
   - Rejection reason tracking

### 5. **Fraud Detection**
   - Automated fraud risk assessment
   - Risk scoring system (0-100)
   - Multiple red flags detection:
     - Duplicate claims
     - Over claims
     - Staged claims
     - Unusual patterns
     - High claim frequency
   - Investigation workflow

### 6. **Commission Module**
   - Agent and broker management
   - Commission calculation based on policies
   - Multiple commission statuses
   - Commission payment tracking
   - Agent performance analytics

## Tech Stack

- **Backend:** Django 4.2.7
- **Database:** SQLite (default, can be configured for PostgreSQL)
- **Frontend:** Bootstrap 5.3.0
- **API:** Django REST Framework 3.14.0
- **Task Queue:** Celery (optional)
- **CORS:** django-cors-headers

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment tool

### Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/kakkarot23/Insurance-ERP.git
cd Insurance-ERP/insurance_erp
```

2. **Create and activate virtual environment:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure database:**
```bash
python manage.py migrate
```

5. **Create superuser:**
```bash
python manage.py createsuperuser
```

6. **Load initial data (optional):**
```bash
python manage.py loaddata initial_data.json
```

7. **Collect static files:**
```bash
python manage.py collectstatic --noinput
```

8. **Run development server:**
```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`

## Usage

### Admin Panel
- Access at `/admin/` with superuser credentials
- Manage all entities and system settings

### Main Application
- Dashboard: `/` - Overview of all modules
- Policies: `/policies/` - Policy management
- Premium: `/policies/premium/` - Premium calculation
- Claims: `/claims/` - Claims processing
- KYC: `/kyc/` - Customer onboarding
- Fraud: `/fraud/` - Fraud detection
- Commissions: `/commissions/` - Commission management

## API Endpoints

The system includes REST API endpoints for:
- Policy CRUD operations
- Claims processing
- KYC verification
- Fraud risk assessment
- Commission calculations

Base URL: `/api/`

## Configuration

### Environment Variables
Create a `.env` file for configuration:
```
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

### Database Configuration
Default: SQLite (db.sqlite3)

For PostgreSQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'insurance_erp',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Project Structure

```
insurance_erp/
├── insurance_erp/         # Main project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── policies/              # Policy management app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── claims/                # Claims processing app
├── kyc/                   # KYC onboarding app
├── fraud/                 # Fraud detection app
├── commissions/           # Commission management app
├── templates/             # HTML templates
├── static/                # CSS, JS, images
├── manage.py
└── requirements.txt
```

## Models Overview

### Policy
- policy_number, policy_type, holder_name, holder_email
- start_date, end_date, status
- premium_amount, sum_insured, coverage_details

### PremiumCalculation
- base_premium, risk_factor, tax_rate, discount_percentage
- total_premium calculation

### Claim
- claim_number, policy reference
- claim_date, incident_date, claim_amount
- status, approved_amount, rejection_reason

### KYCProfile
- full_name, email, phone
- identity_document information
- address details
- verification status

### FraudRisk
- policy reference
- risk_score, risk_level
- red flags detection
- investigation status

### Commission
- agent reference, policy reference
- commission_rate, commission_amount
- status, payment tracking

## Security Features

- User authentication and authorization
- CSRF protection
- SQL injection prevention
- XSS protection
- Secure password handling
- Role-based access control (via Django admin)

## Performance Optimization

- Database query optimization
- Template caching
- Static file compression
- Pagination for large datasets
- Connection pooling (for production)

## Testing

Run tests:
```bash
python manage.py test
```

## Deployment

### Production Checklist
- Set `DEBUG = False`
- Update `SECRET_KEY`
- Configure allowed hosts
- Set up proper database (PostgreSQL recommended)
- Configure email backend
- Enable HTTPS
- Set up static file serving
- Configure logging
- Set up backup strategy

### Using Gunicorn
```bash
pip install gunicorn
gunicorn insurance_erp.wsgi:application --bind 0.0.0.0:8000
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For support, email: support@insuranceerp.com

## Authors

- Insurance ERP Development Team

## Changelog

### Version 1.0.0
- Initial release with all core modules
- Policy lifecycle management
- Premium calculations
- KYC onboarding
- Claims processing
- Fraud detection
- Commission module

## Roadmap

- Mobile application
- Advanced analytics and reporting
- Machine learning fraud detection
- Integration with payment gateways
- API rate limiting
- Enhanced audit logging
- Multi-language support
- Customizable workflows

---

**Last Updated:** December 2024
