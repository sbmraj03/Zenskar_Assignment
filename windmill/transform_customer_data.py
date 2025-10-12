def main(x):
    """
    Transform CSV rows to customer objects.
    Returns list of valid customers for the For loop.
    """
    customers = []  # List to store valid customers
    failed_rows = []  # List to store failed rows for reporting
    
    # Check what type of input we received
    if isinstance(x, dict) and "parsed_data" in x:
        # Input from Parse CSV File step
        rows = x["parsed_data"]
    elif isinstance(x, list):
        # Direct array input
        rows = x
    else:
        # Invalid input, return empty list
        return []
    
    # Process each row from CSV
    for idx, row in enumerate(rows):
        try:
            # Skip rows that aren't dictionaries
            if not isinstance(row, dict):
                failed_rows.append({
                    "row": idx + 1,
                    "error": "Invalid row format",
                    "data": str(row)
                })
                continue
                
            # Get required fields and remove extra spaces
            name = row.get("company_name", "").strip()
            email = row.get("contact_email", "").strip()
            
            # Check if required fields are missing
            if not name or not email:
                missing_fields = []
                if not name:
                    missing_fields.append("company_name")
                if not email:
                    missing_fields.append("contact_email")
                
                # Add to failed rows list
                failed_rows.append({
                    "row": idx + 1,
                    "error": f"Missing required fields: {', '.join(missing_fields)}",
                    "data": row
                })
                continue  # Skip this row
            
            # Create customer object with all fields
            customer = {
                "name": name,
                "email": email,
                "phone": row.get("phone_number", "").strip(),
                "address": row.get("address", "").strip(),
                "city": row.get("city", "").strip(),
                "country": row.get("country", "").strip(),
                "postalCode": row.get("postal_code", "").strip(),
                "taxId": row.get("tax_id", "").strip(),
                "companySize": row.get("company_size", "").strip()
            }
            
            # Add valid customer to our list
            customers.append(customer)
            
        except Exception as e:
            # If anything goes wrong, add to failed rows
            failed_rows.append({
                "row": idx + 1,
                "error": f"Processing error: {str(e)}",
                "data": row if isinstance(row, dict) else str(row)
            })
            continue  # Keep processing other rows
    
    # Save failed rows to file so report step can read them
    import json
    with open('/tmp/failed_rows.json', 'w') as f:
        json.dump(failed_rows, f)
    
    # Return list of valid customers
    return customers
