def main(results):
    """
    Generate processing report with success/failure summary.
    """
    
    # Separate successful and failed API calls
    successful = [r for r in results if r.get("success", False)]
    failed_api = [r for r in results if not r.get("success", False)]
    
    # Load failed rows from transform step (saved by transform script)
    failed_transform = []
    try:
        import json
        with open('/tmp/failed_rows.json', 'r') as f:
            failed_transform = json.load(f)
    except:
        # No failed rows file found, that's okay
        pass
    
    # Calculate numbers for the report
    total_api_calls = len(results)
    success_count = len(successful)
    failed_api_count = len(failed_api)
    failed_transform_count = len(failed_transform)
    total_failed = failed_api_count + failed_transform_count
    
    # Calculate success rate
    total_rows = total_api_calls + failed_transform_count
    success_rate = f"{(success_count/total_rows*100):.1f}%" if total_rows > 0 else "0%"
    
    # Get customer names for the report
    successful_names = [r.get("customer_name", "Unknown") for r in successful]
    failed_api_names = [r.get("customer_name", "Unknown") for r in failed_api]
    
    # Format failed transform rows for display
    failed_transform_details = []
    for row in failed_transform:
        # Handle different data formats
        data = row.get("data", {})
        if isinstance(data, str):
            # Data is stored as string
            company_name = "N/A"
            contact_email = "N/A"
        else:
            # Data is stored as dictionary
            company_name = data.get("company_name", "N/A")
            contact_email = data.get("contact_email", "N/A")
        
        failed_transform_details.append({
            "row": row.get("row", "Unknown"),
            "error": row.get("error", "Unknown error"),
            "company_name": company_name,
            "contact_email": contact_email
        })
    
    # Return complete report
    return {
        "summary": {
            "total_rows_processed": total_rows,
            "successful_api_calls": success_count,
            "failed_api_calls": failed_api_count,
            "failed_transform_rows": failed_transform_count,
            "total_failed": total_failed,
            "success_rate": success_rate
        },
        "successful_customers": successful_names,
        "failed_api_customers": failed_api_names,
        "failed_transform_rows": failed_transform_details,
        "api_results": results
    }