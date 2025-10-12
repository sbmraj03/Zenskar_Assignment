# Developer Guide

## Flow Architecture

```
CSV Input → Parse CSV → Transform Data → For Loop → Send to API → Generate Report
```

## Modifying Transformations

### 1. Access Code

1. Open Windmill: http://localhost:8000
2. Go to Flows → csv_customer_import
3. Click "Transform Customer Data" step
4. Edit code in right panel

### 2. Current Logic

```python
customer = {
    "name": row.get("company_name", "").strip(),
    "email": row.get("contact_email", "").strip(),
    "phone": row.get("phone_number", "").strip(),
    # ... other fields
}
```

### 3. Common Changes

**Add new field:**
```python
customer["website"] = row.get("website", "").strip()
```

**Change column name:**
```python
"name": row.get("business_name", "").strip(),  # was company_name
```

**Add validation:**
```python
if not customer["email"] or "@" not in customer["email"]:
    raise ValueError("Invalid email")
```

**Add data cleaning:**
```python
import re
"phone": re.sub(r'[^\d+]', '', row.get("phone_number", "")),
```

### 4. Testing

1. Modify code
2. Click "Save"
3. Click "Test flow"
4. Upload sample CSV
5. Check results

## Other Modifications

### Change API Endpoint

Edit `sendtomockapi.py`:
```python
api_url = "https://your-api-endpoint.com/customers"
```

### Add Pre-processing

1. Add new step between Parse and Transform
2. Write filtering/sorting logic
3. Update Transform input reference

## Best Practices

- Use `.strip()` to remove whitespace
- Use `.get()` with defaults
- Keep validation in try-except blocks
- Test with edge cases
- Don't change function signatures