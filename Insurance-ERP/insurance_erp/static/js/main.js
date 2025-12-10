// Main JavaScript for Insurance ERP

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips if using Bootstrap
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Add form validation
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
});

// Utility function for formatting currency
function formatCurrency(value) {
    return '₹' + parseFloat(value).toLocaleString('en-IN', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });
}

// Utility function for formatting date
function formatDate(date) {
    return new Date(date).toLocaleDateString('en-IN', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    });
}

// Calculate premium on form change
function calculatePremium() {
    const basePremium = parseFloat(document.getElementById('base_premium')?.value || 0);
    const riskFactor = parseFloat(document.getElementById('risk_factor')?.value || 1);
    const taxRate = parseFloat(document.getElementById('tax_rate')?.value || 0);
    const discount = parseFloat(document.getElementById('discount_percentage')?.value || 0);

    const taxable = basePremium * riskFactor;
    const tax = taxable * (taxRate / 100);
    const discountAmount = (taxable + tax) * (discount / 100);
    const total = taxable + tax - discountAmount;

    const totalElement = document.getElementById('total_premium_display');
    if (totalElement) {
        totalElement.textContent = formatCurrency(total);
    }
}

// Attach event listeners for premium calculation
document.addEventListener('DOMContentLoaded', function() {
    ['base_premium', 'risk_factor', 'tax_rate', 'discount_percentage'].forEach(id => {
        const element = document.getElementById(id);
        if (element) {
            element.addEventListener('change', calculatePremium);
            element.addEventListener('input', calculatePremium);
        }
    });
});

// Confirm delete action
function confirmDelete(message = 'Are you sure you want to delete this item?') {
    return confirm(message);
}

// Export table to CSV
function exportTableToCSV(filename = 'export.csv') {
    const table = document.querySelector('table');
    let csv = [];
    
    for (let row of table.rows) {
        let rowData = [];
        for (let cell of row.cells) {
            rowData.push('"' + cell.innerText.replace(/"/g, '""') + '"');
        }
        csv.push(rowData.join(','));
    }
    
    downloadCSV(csv.join('\n'), filename);
}

function downloadCSV(csv, filename) {
    let csvFile = new Blob([csv], { type: 'text/csv' });
    let downloadLink = document.createElement('a');
    downloadLink.href = URL.createObjectURL(csvFile);
    downloadLink.download = filename;
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
}
