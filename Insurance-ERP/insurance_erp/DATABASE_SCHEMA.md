# Insurance ERP - Database Schema Documentation

## Complete Model Reference

---

## 1. POLICIES Module

### Policy Model
**Purpose:** Store insurance policy information

**Fields:**
```
- policy_number (CharField, unique)
- policy_type (Choice: LIFE, HEALTH, AUTO, PROPERTY, MARINE)
- holder_name (CharField)
- holder_email (EmailField)
- holder_phone (CharField)
- start_date (DateField)
- end_date (DateField)
- status (Choice: DRAFT, ACTIVE, SUSPENDED, EXPIRED, CANCELLED)
- premium_amount (DecimalField)
- sum_insured (DecimalField)
- coverage_details (TextField)
- created_at (DateTimeField, auto_now_add)
- updated_at (DateTimeField, auto_now)
- created_by (ForeignKey: User)
```

**Relationships:**
- One-to-One: PremiumCalculation
- One-to-Many: Claim
- One-to-Many: FraudRisk
- One-to-Many: Commission

---

### PremiumCalculation Model
**Purpose:** Store premium calculation details for policies

**Fields:**
```
- policy (OneToOneField: Policy)
- base_premium (DecimalField)
- risk_factor (DecimalField, default=1.0)
- tax_rate (DecimalField, default=18.0)
- discount_percentage (DecimalField, default=0.0)
- total_premium (DecimalField)
- calculated_at (DateTimeField, auto_now)
- notes (TextField, blank)
```

**Methods:**
- `calculate_total()` - Calculates total premium with tax and discount

**Formula:**
```
taxable = base_premium * risk_factor
tax = taxable * (tax_rate / 100)
discount = (taxable + tax) * (discount_percentage / 100)
total_premium = taxable + tax - discount
```

---

## 2. CLAIMS Module

### Claim Model
**Purpose:** Manage insurance claim records

**Fields:**
```
- claim_number (CharField, unique)
- policy (ForeignKey: Policy)
- claim_date (DateField)
- incident_date (DateField)
- claim_amount (DecimalField)
- description (TextField)
- status (Choice: FILED, UNDER_REVIEW, APPROVED, REJECTED, PAID)
- approved_amount (DecimalField, null/blank)
- rejection_reason (TextField, blank)
- assignee (ForeignKey: User, null/blank)
- created_at (DateTimeField, auto_now_add)
- updated_at (DateTimeField, auto_now)
```

**Relationships:**
- Many-to-One: Policy
- One-to-Many: ClaimDocument
- One-to-One: FraudRisk (optional)

---

### ClaimDocument Model
**Purpose:** Store claim attachments and documents

**Fields:**
```
- claim (ForeignKey: Claim)
- document_type (CharField)
- file (FileField, upload_to='claim_documents/')
- uploaded_at (DateTimeField, auto_now_add)
```

**Relationships:**
- Many-to-One: Claim

---

## 3. KYC Module

### KYCProfile Model
**Purpose:** Store customer KYC verification information

**Fields:**
```
- id (UUIDField, primary_key)
- full_name (CharField)
- email (EmailField, unique)
- phone (CharField)
- kyc_type (Choice: INDIVIDUAL, CORPORATE, PARTNERSHIP)
- status (Choice: PENDING, VERIFIED, REJECTED, EXPIRED)

Identity Documents:
- identity_document_type (CharField)
- identity_document_number (CharField)
- identity_document_file (FileField)
- identity_verified_at (DateTimeField, null/blank)

Address:
- address_line1 (CharField)
- address_line2 (CharField, blank)
- city (CharField)
- state (CharField)
- postal_code (CharField)
- country (CharField, default='India')

Additional:
- address_proof_file (FileField, null/blank)
- pan_card (CharField, blank)
- aadhar_number (CharField, blank)
- verified_by (ForeignKey: User, null/blank)
- verification_notes (TextField, blank)
- created_at (DateTimeField, auto_now_add)
- updated_at (DateTimeField, auto_now)
```

**Relationships:**
- Many-to-One: User (verified_by)

---

## 4. FRAUD Detection Module

### FraudRisk Model
**Purpose:** Detect and track fraudulent claims

**Fields:**
```
- claim (OneToOneField: Claim, optional)
- policy (ForeignKey: Policy)
- risk_score (IntegerField, 0-100)
- risk_level (Choice: LOW, MEDIUM, HIGH, CRITICAL)
- status (Choice: FLAGGED, UNDER_INVESTIGATION, CONFIRMED, CLEARED, CLOSED)

Red Flags:
- is_duplicate_claim (BooleanField)
- is_over_claim (BooleanField)
- is_staged_claim (BooleanField)
- unusual_pattern (BooleanField)
- high_claim_frequency (BooleanField)

Details:
- description (TextField)
- investigation_notes (TextField, blank)
- assigned_to (ForeignKey: User, null/blank)
- created_at (DateTimeField, auto_now_add)
- updated_at (DateTimeField, auto_now)
```

**Methods:**
- `calculate_risk_score()` - Auto-calculates fraud risk score based on flags

**Scoring Logic:**
```
Duplicate Claim = +30
Over Claim = +25
Staged Claim = +35
Unusual Pattern = +20
High Frequency = +15

Risk Levels:
< 30 = LOW
30-49 = MEDIUM
50-79 = HIGH
80+ = CRITICAL
```

**Relationships:**
- Many-to-One: Policy
- One-to-One: Claim (optional)
- Many-to-One: User (assigned_to)

---

## 5. COMMISSIONS Module

### Agent Model
**Purpose:** Store information about insurance agents/brokers

**Fields:**
```
- agent_code (CharField, unique)
- name (CharField)
- email (EmailField)
- phone (CharField)
- agent_type (Choice: INDIVIDUAL, AGENCY, BROKER)
- commission_rate (DecimalField, default=5.0)
- is_active (BooleanField, default=True)
- created_at (DateTimeField, auto_now_add)
- updated_at (DateTimeField, auto_now)
```

**Relationships:**
- One-to-Many: Commission

---

### Commission Model
**Purpose:** Track commissions earned on policies

**Fields:**
```
- commission_number (CharField, unique)
- agent (ForeignKey: Agent)
- policy (ForeignKey: Policy)
- commission_rate (DecimalField)
- base_amount (DecimalField)
- commission_amount (DecimalField)
- status (Choice: PENDING, APPROVED, PAID, REVERSED)
- commission_date (DateField)
- payment_date (DateField, null/blank)
- created_at (DateTimeField, auto_now_add)
- updated_at (DateTimeField, auto_now)
```

**Methods:**
- `calculate_commission()` - Calculates commission amount

**Formula:**
```
commission_amount = base_amount * (commission_rate / 100)
```

**Relationships:**
- Many-to-One: Agent
- Many-to-One: Policy
- One-to-Many: CommissionPayment

---

### CommissionPayment Model
**Purpose:** Track commission payments to agents

**Fields:**
```
- payment_id (CharField, unique)
- commission (ForeignKey: Commission)
- amount (DecimalField)
- payment_method (Choice: BANK_TRANSFER, CHECK, CASH, OTHERS)
- payment_date (DateField)
- reference_number (CharField, blank)
- remarks (TextField, blank)
- created_at (DateTimeField, auto_now_add)
```

**Relationships:**
- Many-to-One: Commission

---

## Entity Relationship Diagram

```
┌─────────────────┐
│     User        │
└─────────────────┘
        △ △ △
        │ │ └─── created_by
        │ └───── verified_by
        └─────── assigned_to

┌─────────────────┐
│    Policy       │◄──────────┐
└─────────────────┘           │
        │                      │
        ├─ Claim ──────────────┤
        │                      │
        ├─ FraudRisk ──────────┘
        │
        └─ Commission
                │
                └─ CommissionPayment

┌─────────────────┐
│   Agent         │
└─────────────────┘
        │
        └─ Commission

┌─────────────────┐
│   KYCProfile    │
└─────────────────┘

┌─────────────────┐
│     Claim       │
└─────────────────┘
        │
        ├─ ClaimDocument
        │
        └─ FraudRisk
```

---

## Data Relationships Summary

| From | To | Type | Field |
|------|----|----|-------|
| Policy | User | Foreign Key | created_by |
| Policy | Claim | One-to-Many | - |
| Policy | FraudRisk | One-to-Many | - |
| Policy | Commission | One-to-Many | - |
| Policy | PremiumCalculation | One-to-One | - |
| Claim | ClaimDocument | One-to-Many | - |
| Claim | FraudRisk | One-to-One | - |
| Agent | Commission | One-to-Many | - |
| Commission | CommissionPayment | One-to-Many | - |
| FraudRisk | User | Foreign Key | assigned_to |
| KYCProfile | User | Foreign Key | verified_by |

---

## Field Types Reference

| Type | Usage | Example |
|------|-------|---------|
| CharField | Short text | "John Doe" |
| EmailField | Email addresses | "john@example.com" |
| DateField | Dates only | 2024-12-09 |
| DateTimeField | Date and time | 2024-12-09 14:30:00 |
| DecimalField | Money/Numbers | 10000.50 |
| IntegerField | Whole numbers | 75 |
| BooleanField | True/False | True |
| TextField | Long text | Policy coverage details |
| FileField | File uploads | Document PDFs |
| ForeignKey | Relationships | link to User |
| OneToOneField | Unique relationship | Policy ↔ Premium |
| UUIDField | Unique ID | UUID value |
| Choice | Dropdown options | ACTIVE, DRAFT, etc |

---

## Validation Rules

### Policy
- policy_number: Required, unique
- start_date < end_date
- premium_amount >= 0
- sum_insured > 0

### Claim
- claim_date >= created_at
- incident_date <= claim_date
- claim_amount > 0

### KYCProfile
- email: Unique
- pan_card: Unique (if provided)
- aadhar_number: Unique (if provided)

### FraudRisk
- risk_score: 0-100
- At least one red flag

### Commission
- commission_rate > 0
- base_amount >= 0
- commission_amount >= 0

---

## Indexes Created

### Performance Optimization
```
- Policy.policy_number (unique)
- Policy.status
- Policy.created_at

- Claim.claim_number (unique)
- Claim.status
- Claim.policy_id

- KYCProfile.email (unique)
- KYCProfile.status

- FraudRisk.risk_score (ordering)
- FraudRisk.status

- Agent.agent_code (unique)

- Commission.commission_number (unique)
- Commission.status
```

---

## Total Database Statistics

| Metric | Count |
|--------|-------|
| **Models** | 9 |
| **Fields** | 150+ |
| **Relationships** | 20+ |
| **Foreign Keys** | 12 |
| **One-to-One** | 2 |
| **One-to-Many** | 8 |
| **Unique Fields** | 15+ |
| **Choices** | 20+ |

---

## Migration Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migrations
python manage.py showmigrations

# Revert specific migration
python manage.py migrate app_name 0001
```

---

**Last Updated:** December 2024  
**Django Version:** 4.2.7  
**Database:** SQLite (Default) / PostgreSQL (Production)
