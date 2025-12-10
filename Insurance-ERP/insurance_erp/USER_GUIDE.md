# Insurance ERP - User Guide

## How to Use Each Module

---

## 🏠 Dashboard

**Location:** `http://127.0.0.1:8000/`

The main dashboard provides quick access to all 6 modules with description cards.

### Features:
- Color-coded module cards
- Quick navigation links
- Module descriptions
- Call-to-action buttons

---

## 📋 Module 1: Policy Lifecycle Management

**Location:** `http://127.0.0.1:8000/policies/`

### 1.1 View Policies
1. Click **"Policies"** in navigation
2. See list of all policies with:
   - Policy number
   - Holder name
   - Policy type
   - Status badge
   - Premium amount
   - Created date

### 1.2 Create New Policy
1. Click **"New Policy"** button
2. Fill in the form:
   - **Policy Number** - Unique identifier
   - **Policy Type** - Choose from 5 options
   - **Holder Name** - Customer name
   - **Holder Email** - Customer email
   - **Holder Phone** - Contact number
   - **Start Date** - Policy effective date
   - **End Date** - Policy expiry date
   - **Status** - Initial status (Draft)
   - **Premium Amount** - Initial premium
   - **Sum Insured** - Coverage amount
   - **Coverage Details** - Policy terms
3. Click **"Save Policy"**

### 1.3 View Policy Details
1. Click **"View"** button on any policy
2. See complete information:
   - Policy details
   - Holder information
   - Coverage details
   - Premium calculation (if available)
   - Action buttons

### 1.4 Edit Policy
1. Click **"Edit"** button on policy list or detail
2. Modify any fields
3. Click **"Save Policy"**

### 1.5 Calculate Premium
1. Click **"Premium Calculator"** button
2. Select a policy from dropdown
3. Enter calculation details:
   - **Base Premium** - Starting amount
   - **Risk Factor** - Default 1.0, adjust based on risk
   - **Tax Rate** - Default 18%, adjust as needed
   - **Discount %** - Any discount to apply
4. Click **"Calculate & Save"**
5. See auto-calculated total premium
6. System automatically updates policy premium

### Status Workflow:
```
DRAFT → ACTIVE → SUSPENDED → EXPIRED
                 ↓
              CANCELLED
```

---

## 💰 Module 2: Premium Calculations

**Location:** `http://127.0.0.1:8000/policies/premium/`

### Features:
- Real-time calculation
- Recent calculations history
- Policy selection
- Form validation

### Calculation Formula:
```
Taxable Amount = Base Premium × Risk Factor
Tax Amount = Taxable Amount × (Tax Rate / 100)
Discount Amount = (Taxable + Tax) × (Discount % / 100)
Total Premium = Taxable + Tax - Discount
```

### Example:
```
Base Premium:     ₹10,000
Risk Factor:      1.5
Tax Rate:         18%
Discount %:       5%

Calculation:
Taxable = 10,000 × 1.5 = ₹15,000
Tax = 15,000 × 0.18 = ₹2,700
Discount = (15,000 + 2,700) × 0.05 = ₹885
Total = 15,000 + 2,700 - 885 = ₹16,815
```

### How to Calculate:
1. Go to Premium Calculator
2. Select policy
3. Enter base premium
4. Adjust risk factor (higher = more premium)
5. Set tax rate
6. Add discount if applicable
7. Click "Calculate & Save"
8. Policy premium updates automatically

---

## 👤 Module 3: KYC Onboarding

**Location:** `http://127.0.0.1:8000/kyc/`

### 3.1 View KYC Profiles
1. Click **"KYC"** in navigation
2. See list of all KYC profiles with:
   - Customer name
   - Email
   - Phone
   - Entity type
   - Status badge

### 3.2 Create New KYC Profile
1. Click **"New KYC Profile"** button
2. Fill in personal information:
   - **Full Name** - Customer name
   - **Email** - Unique email
   - **Phone** - Contact number
   - **KYC Type** - Individual/Corporate/Partnership
3. Add identity documents:
   - **Document Type** - Passport, License, etc.
   - **Document Number** - ID number
   - **Document File** - Upload scan/photo
4. Enter address:
   - **Address Line 1** - Street address
   - **Address Line 2** - Optional
   - **City** - City name
   - **State** - State/Province
   - **Postal Code** - ZIP code
   - **Country** - Country (default: India)
5. Add additional documents:
   - **Address Proof** - Utility bill, lease, etc.
   - **PAN Card** - Tax ID
   - **Aadhar Number** - ID number
6. Click **"Save KYC Profile"**

### 3.3 View KYC Profile Details
1. Click **"View"** button on any profile
2. See:
   - Personal information
   - Identity details
   - Address information
   - Verification status

### 3.4 Verify KYC
1. Click **"Verify"** button on profile
2. Review submitted documents
3. Choose action:
   - **Approved** - Mark as VERIFIED
   - **Rejected** - Mark as REJECTED
4. Add verification notes
5. Click **"Save Verification"**

### Status Workflow:
```
PENDING → VERIFIED
        ↓
       REJECTED
        ↓
       EXPIRED
```

### Entity Types:
- **Individual** - Single person
- **Corporate** - Company/Business
- **Partnership** - Multiple partners

---

## 📄 Module 4: Claims Processing

**Location:** `http://127.0.0.1:8000/claims/`

### 4.1 View Claims
1. Click **"Claims"** in navigation
2. See list of all claims with:
   - Claim number
   - Policy reference
   - Claim date
   - Claim amount
   - Status badge

### 4.2 File New Claim
1. Click **"New Claim"** button
2. Fill in claim details:
   - **Claim Number** - Unique claim ID
   - **Policy** - Select from dropdown
   - **Claim Date** - When claim was filed
   - **Incident Date** - When incident occurred
   - **Claim Amount** - Amount claimed
   - **Description** - Claim description
3. Click **"Save Claim"**

### 4.3 View Claim Details
1. Click **"View"** button on any claim
2. See:
   - Claim information
   - Policy details
   - Claim amount
   - Status and approval details

### 4.4 Approve/Reject Claim
1. Click **"Approve"** button on claim
2. Choose action:
   - **Approve** - Enter approved amount
   - **Reject** - Enter rejection reason
3. Add notes
4. Click **"Save Decision"**

### 4.5 Upload Documents
- Create claim first
- Documents can be attached in admin panel

### Status Workflow:
```
FILED → UNDER_REVIEW → APPROVED → PAID
                    ↓
                 REJECTED
```

### Processing Steps:
1. **FILED** - Claim submitted
2. **UNDER_REVIEW** - Being processed
3. **APPROVED** - Claim accepted (amount set)
4. **REJECTED** - Claim denied (reason documented)
5. **PAID** - Payment processed

---

## 🛡️ Module 5: Fraud Detection

**Location:** `http://127.0.0.1:8000/fraud/`

### 5.1 View Fraud Risks
1. Click **"Fraud"** in navigation
2. See list sorted by risk score:
   - Policy reference
   - Risk score (0-100)
   - Risk level badge
   - Status
   - Actions

### 5.2 Flag Fraud Risk
1. Click **"Flag Fraud Risk"** button
2. Select policy
3. Select red flags that apply:
   - ☐ **Duplicate Claim** - Same claim filed multiple times
   - ☐ **Over Claim** - Claim exceeds coverage
   - ☐ **Staged Claim** - Intentional incident
   - ☐ **Unusual Pattern** - Atypical claim pattern
   - ☐ **High Frequency** - Too many claims
4. Describe the fraud suspicion
5. Click **"Save Fraud Risk"**
6. System auto-calculates risk score

### 5.3 View Risk Details
1. Click **"View"** button on fraud risk
2. See:
   - Risk assessment details
   - Risk score and level
   - Red flags marked
   - Description
   - Investigation notes

### 5.4 Investigate Fraud
1. Click **"Investigate"** button
2. Choose status:
   - **UNDER_INVESTIGATION** - Being investigated
   - **CONFIRMED** - Fraud confirmed
   - **CLEARED** - No fraud found
   - **CLOSED** - Investigation complete
3. Add investigation notes
4. Click **"Save Investigation"**

### Risk Scoring Algorithm:
```
Duplicate Claim = +30 points
Over Claim = +25 points
Staged Claim = +35 points
Unusual Pattern = +20 points
High Frequency = +15 points

RISK LEVELS:
0-29 = LOW 🟢
30-49 = MEDIUM 🟡
50-79 = HIGH 🟠
80-100 = CRITICAL 🔴
```

### Example:
```
Flags Checked:
- Duplicate Claim ✓ (+30)
- Over Claim ✓ (+25)
- Unusual Pattern ✓ (+20)

Total Score = 30 + 25 + 20 = 75
Risk Level = HIGH 🟠
```

### Status Workflow:
```
FLAGGED → UNDER_INVESTIGATION → CONFIRMED → CLOSED
                             ↓
                            CLEARED
```

---

## 💵 Module 6: Commission Module

**Location:** `http://127.0.0.1:8000/commissions/`

### 6.1 Dashboard Overview
1. Click **"Commissions"** in navigation
2. See dashboard with:
   - Total commission amount
   - Amount paid
   - Pending amount
   - Number of agents
   - Recent agent list
   - Recent commissions

### 6.2 Manage Agents

#### View Agents:
1. Click **"Agents"** tab
2. See all agents with:
   - Agent code
   - Name
   - Agent type
   - Commission rate

#### Add New Agent:
1. Click **"New Agent"** button
2. Fill in details:
   - **Agent Code** - Unique code
   - **Name** - Agent name
   - **Email** - Email address
   - **Phone** - Contact number
   - **Agent Type** - Individual/Agency/Broker
   - **Commission Rate** - % commission (e.g., 5%)
   - **Is Active** - Toggle active status
3. Click **"Save Agent"**

#### View Agent Details:
1. Click agent name
2. See:
   - Agent information
   - Commission history
   - Total earned
   - Recent commissions

### 6.3 Manage Commissions

#### View Commissions:
1. Click **"Commissions"** tab
2. See all commissions with:
   - Commission number
   - Agent name
   - Commission amount
   - Status badge

#### Create Commission:
1. Click **"New Commission"** button
2. Fill in details:
   - **Commission Number** - Unique ID
   - **Agent** - Select from dropdown
   - **Policy** - Select from dropdown
   - **Commission Rate** - % commission
   - **Base Amount** - Amount commission calculated on
   - **Commission Date** - Commission date
3. Click **"Calculate & Save"**
4. System auto-calculates commission amount

#### Commission Calculation:
```
Commission Amount = Base Amount × (Commission Rate / 100)

Example:
Base Amount = ₹10,000
Commission Rate = 5%
Commission Amount = 10,000 × 0.05 = ₹500
```

### 6.4 Track Payments
- Payments managed in admin panel
- Track by status: Pending, Approved, Paid, Reversed

### Agent Types:
- **Individual Agent** - Single insurance agent
- **Insurance Agency** - Agency with multiple agents
- **Insurance Broker** - Broker firm

### Commission Status Workflow:
```
PENDING → APPROVED → PAID
            ↓
         REVERSED
```

---

## 🔧 Admin Panel

**Location:** `http://127.0.0.1:8000/admin/`

Access with superuser credentials.

### Admin Features:
- Add/Edit/Delete any record
- Filter by status, date, type
- Search by name, number, email
- View relationships
- Bulk actions
- Change logs

### Admin Access:
1. Go to `/admin/`
2. Login with superuser credentials
3. Select model to manage
4. Perform CRUD operations

---

## 📊 Common Tasks

### Create Complete Policy Workflow:
1. **Create Policy** → Policies → New Policy
2. **Calculate Premium** → Policies → Premium Calculator
3. **Add KYC** (if new customer) → KYC → New Profile
4. **Verify KYC** → KYC → Select profile → Verify
5. **File Claim** (when needed) → Claims → New Claim
6. **Process Claim** → Claims → Approve
7. **Track Commission** → Commissions → Add agent → Add commission

### Fraud Investigation Workflow:
1. **Flag Risk** → Fraud → Flag Fraud Risk
2. **Review** → Fraud → View details
3. **Investigate** → Fraud → Investigate
4. **Document** → Add investigation notes
5. **Conclude** → Set final status

### Commission Workflow:
1. **Add Agent** → Commissions → New Agent
2. **Create Commission** → Commissions → New Commission
3. **Track Payment** → Admin Panel → Commission Payment

---

## 📈 Best Practices

### Policy Management:
- Set realistic start/end dates
- Ensure premium > 0
- Keep coverage details detailed
- Update status appropriately

### Premium Calculation:
- Review risk factors carefully
- Consider market conditions for tax
- Document discount reasons
- Save calculations for records

### KYC Verification:
- Verify documents thoroughly
- Check for consistency
- Document verification process
- Follow compliance requirements

### Claim Processing:
- Verify claim details
- Cross-reference with policy
- Check for fraud indicators
- Document approval/rejection

### Fraud Detection:
- Mark suspicious claims
- Review fraud indicators
- Investigate thoroughly
- Document findings

### Commission Management:
- Ensure accurate rates
- Calculate timely
- Track payments
- Reconcile regularly

---

## ⚠️ Important Notes

### Required Fields:
- All marked with asterisk (*)
- Must be filled to save

### Data Types:
- **Dates** - Use date picker
- **Numbers** - Enter decimals as needed
- **Emails** - Must be valid email format
- **Phone** - Any format accepted
- **Files** - PDF, JPG, PNG supported

### Unique Fields:
- Policy number - Cannot duplicate
- Email - Cannot duplicate in KYC
- Agent code - Cannot duplicate
- Commission number - Cannot duplicate

---

## 🆘 Troubleshooting

### Form Won't Save:
1. Check all required fields are filled (*)
2. Verify email format if applicable
3. Check for duplicate values
4. Look for validation error messages

### Data Not Appearing:
1. Refresh page (F5)
2. Check filters/search
3. Ensure item was saved
4. Check pagination

### Can't Access Module:
1. Ensure logged in
2. Check URL spelling
3. Clear browser cache
4. Try different browser

---

## 📞 Support

For detailed information:
- See **README.md** for complete documentation
- See **DATABASE_SCHEMA.md** for data structure
- See **QUICKSTART.md** for setup help
- See **DEPLOYMENT.md** for deployment

---

**Last Updated:** December 2024  
**Version:** 1.0.0
