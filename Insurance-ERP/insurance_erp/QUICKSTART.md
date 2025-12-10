# Insurance ERP - Quick Start Guide

## Project Overview

A complete Django-based Insurance ERP system with 6 core modules:
1. ✅ Policy Lifecycle
2. ✅ Premium Calculations
3. ✅ KYC Onboarding
4. ✅ Claims Processing
5. ✅ Fraud Detection
6. ✅ Commission Module

## Quick Setup (5 minutes)

### Step 1: Navigate to Project
```bash
cd d:\Insurance ERP\insurance_erp
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations
```bash
python manage.py migrate
```

### Step 5: Create Admin User
```bash
python manage.py createsuperuser
# Follow the prompts to create your admin account
```

### Step 6: Run Server
```bash
python manage.py runserver
```

### Step 7: Access Application
- Main App: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

## Project Structure

```
insurance_erp/
│
├── manage.py                    # Django management command
├── requirements.txt             # Python dependencies
├── README.md                    # Full documentation
├── .gitignore                   # Git ignore rules
│
├── insurance_erp/               # Main project settings
│   ├── settings.py              # Django settings
│   ├── urls.py                  # URL routing
│   ├── views.py                 # Main views
│   ├── wsgi.py                  # WSGI configuration
│   └── asgi.py                  # ASGI configuration
│
├── policies/                    # Policy Management Module
│   ├── models.py                # Policy & PremiumCalculation models
│   ├── views.py                 # Policy views
│   ├── forms.py                 # Policy forms
│   ├── urls.py                  # Policy URLs
│   ├── admin.py                 # Admin interface
│   └── apps.py                  # App configuration
│
├── claims/                      # Claims Processing Module
│   ├── models.py                # Claim & ClaimDocument models
│   ├── views.py                 # Claim views
│   ├── forms.py                 # Claim forms
│   ├── urls.py                  # Claim URLs
│   ├── admin.py                 # Admin interface
│   └── apps.py                  # App configuration
│
├── kyc/                         # KYC Onboarding Module
│   ├── models.py                # KYCProfile model
│   ├── views.py                 # KYC views
│   ├── forms.py                 # KYC forms
│   ├── urls.py                  # KYC URLs
│   ├── admin.py                 # Admin interface
│   └── apps.py                  # App configuration
│
├── fraud/                       # Fraud Detection Module
│   ├── models.py                # FraudRisk model
│   ├── views.py                 # Fraud views
│   ├── forms.py                 # Fraud forms
│   ├── urls.py                  # Fraud URLs
│   ├── admin.py                 # Admin interface
│   └── apps.py                  # App configuration
│
├── commissions/                 # Commission Module
│   ├── models.py                # Agent, Commission, CommissionPayment models
│   ├── views.py                 # Commission views
│   ├── forms.py                 # Commission forms
│   ├── urls.py                  # Commission URLs
│   ├── admin.py                 # Admin interface
│   └── apps.py                  # App configuration
│
├── templates/                   # HTML Templates
│   ├── base.html                # Base template
│   ├── dashboard.html           # Dashboard
│   ├── policies/
│   │   ├── policy_list.html
│   │   ├── policy_detail.html
│   │   ├── policy_form.html
│   │   └── premium_calculation.html
│   ├── claims/
│   │   ├── claim_list.html
│   │   ├── claim_detail.html
│   │   ├── claim_form.html
│   │   └── claim_approval.html
│   ├── kyc/
│   │   ├── kyc_list.html
│   │   ├── kyc_detail.html
│   │   ├── kyc_form.html
│   │   └── kyc_verification.html
│   ├── fraud/
│   │   ├── fraud_list.html
│   │   ├── fraud_detail.html
│   │   ├── fraud_form.html
│   │   └── fraud_investigation.html
│   └── commissions/
│       └── commission_dashboard.html
│
└── static/                      # Static Files
    ├── css/
    │   └── style.css            # Main stylesheet
    └── js/
        └── main.js              # Main JavaScript

```

## Module Details

### 1. Policy Lifecycle
**File:** `policies/`
- Create and manage insurance policies
- Track policy status: Draft → Active → Expired
- Supports: Life, Health, Auto, Property, Marine
- **URL:** `/policies/`

### 2. Premium Calculations
**File:** `policies/models.py - PremiumCalculation`
- Calculate premiums with risk factors
- Apply taxes and discounts
- Formula: `(Base × RiskFactor × (1 + Tax%)) - Discount`
- **URL:** `/policies/premium/`

### 3. KYC Onboarding
**File:** `kyc/`
- Customer verification process
- Supports Individual, Corporate, Partnership
- Document uploads (Identity, Address proof, PAN, Aadhar)
- **URL:** `/kyc/`

### 4. Claims Processing
**File:** `claims/`
- File and track claims
- Status: Filed → Under Review → Approved → Paid
- Approval workflow with amount verification
- **URL:** `/claims/`

### 5. Fraud Detection
**File:** `fraud/`
- Automated fraud risk scoring (0-100)
- Red flags: Duplicate, Over-claim, Staged, Unusual pattern, High frequency
- Risk levels: LOW, MEDIUM, HIGH, CRITICAL
- **URL:** `/fraud/`

### 6. Commission Module
**File:** `commissions/`
- Agent and broker management
- Commission calculation on policies
- Payment tracking
- **URL:** `/commissions/`

## Key Features

### Authentication & Security
- Django admin authentication
- CSRF protection
- SQL injection prevention
- XSS protection

### Frontend
- Responsive Bootstrap 5 design
- Mobile-friendly interface
- Interactive forms
- Real-time calculations

### Database
- SQLite (default)
- Support for PostgreSQL
- Automatic migrations
- Data relationships and constraints

### API-Ready
- Django REST Framework integration
- CORS enabled
- Pagination support
- Authentication ready

## Admin Panel Features

Access `/admin/` to:
- Manage all entities
- View relationships
- Edit records in-place
- Filter and search
- Bulk actions
- Change logs

## Common Tasks

### Add a New Policy
1. Navigate to `/policies/`
2. Click "New Policy"
3. Fill in policy details
4. Click "Save Policy"

### Calculate Premium
1. Go to `/policies/premium/`
2. Select a policy
3. Enter base premium, risk factor, tax rate, discount
4. Click "Calculate & Save"

### Process a Claim
1. Navigate to `/claims/`
2. Click "New Claim"
3. Select policy and enter claim details
4. Click "Save Claim"
5. Later, click "Approve" to process

### Verify KYC
1. Go to `/kyc/`
2. Select a profile
3. Click "Verify"
4. Enter verification notes and approve/reject
5. Save

### Flag Fraud
1. Navigate to `/fraud/`
2. Click "Flag Fraud Risk"
3. Select policy and check red flags
4. System auto-calculates risk score
5. Assign for investigation

### Manage Commissions
1. Go to `/commissions/`
2. View dashboard with totals
3. Add agents or create commissions
4. Track payments

## Configuration

### Environment Variables
Create `.env` file in project root:
```
DEBUG=True
SECRET_KEY=your-secret-key-change-in-production
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### Database
Default: SQLite (`db.sqlite3`)

To use PostgreSQL:
```python
# settings.py
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

## Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test policies

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

## Troubleshooting

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Database Error
```bash
# Reset database
python manage.py migrate
python manage.py migrate --fake
```

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

### Admin Password Reset
```bash
python manage.py changepassword admin
```

## Production Deployment

### Using Gunicorn
```bash
pip install gunicorn
gunicorn insurance_erp.wsgi:application --bind 0.0.0.0:8000
```

### Using Docker
```dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "insurance_erp.wsgi:application", "--bind", "0.0.0.0:8000"]
```

### Checklist
- [ ] Set `DEBUG = False`
- [ ] Change `SECRET_KEY`
- [ ] Update `ALLOWED_HOSTS`
- [ ] Use PostgreSQL
- [ ] Configure email
- [ ] Enable HTTPS
- [ ] Set up logging
- [ ] Configure backups
- [ ] Use Gunicorn/uWSGI
- [ ] Use Nginx as reverse proxy

## Support & Documentation

- Full docs: See `README.md`
- Django docs: https://docs.djangoproject.com/
- Bootstrap docs: https://getbootstrap.com/docs/

## Next Steps

1. ✅ Project Setup
2. ✅ Create Superuser
3. ✅ Run Server
4. ✅ Access Admin Panel
5. → Create sample data
6. → Test all modules
7. → Customize styling
8. → Deploy to production

---

**Happy coding! 🚀**
