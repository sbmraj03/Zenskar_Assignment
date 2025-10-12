# User Guide

## How to Use

### 1. Upload CSV File

1. Go to http://localhost:8000
2. Find "csv_customer_import" flow
3. Click "Run"
4. Choose your CSV file
5. Click "Run" to start

### 2. Monitor Progress

- Green checkmarks = Success
- Red X = Failed
- Progress bar shows completion

### 3. Review Results

Get detailed report with:
- Total customers processed
- Success/failure counts
- Customer names
- Error details

## CSV Format

**Required columns:**
```
company_name,contact_email
```

**Optional columns:**
```
contact_first_name,contact_last_name,phone_number,address,city,country,postal_code,tax_id,company_size
```

## Example CSV

```csv
company_name,contact_email,phone_number,address,city,country
Acme Corp,john@acme.com,+1-555-0100,123 Main St,New York,USA
Beta Inc,jane@beta.co,+1-555-0200,456 Oak Ave,San Francisco,USA
```

## Common Issues

**Missing required fields**
- Ensure company_name and contact_email are filled

**Invalid email**
- Check email has @ symbol and valid domain

**File upload fails**
- Save as CSV format (not Excel)
- Use UTF-8 encoding
- Keep file under 10MB

## Best Practices

- Test with small files first
- Check results before uploading more
- Fix errors and re-upload failed rows
- Keep consistent data format