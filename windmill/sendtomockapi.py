import requests

def main(customer):
    """
    Send customer data to MockAPI.
    Returns success/failure result.
    """
    
    # Windmill For loop wraps data in a 'value' key
    if isinstance(customer, dict) and "value" in customer:
        # Extract actual customer data from For loop wrapper
        customer_data = customer["value"]
        customer_name = customer_data.get("name", "Unknown")
    else:
        # Direct customer data (fallback)
        customer_data = customer
        customer_name = customer.get("name", "Unknown")
    
    # MockAPI endpoint - replace with your project ID
    api_url = "https://mockapi.io/api/v1/your_project_id/customers"
    
    try:
        # Send POST request to MockAPI
        response = requests.post(
            api_url,
            json=customer_data,  # Send customer data as JSON
            headers={"Content-Type": "application/json"},
            timeout=30  # Wait max 30 seconds
        )
        
        # Check if request was successful
        success = response.status_code in [200, 201]
        
        # Return result for report generation
        return {
            "success": success,
            "customer_name": customer_name,
            "status_code": response.status_code,
            "response": response.text if not success else "Success"
        }
        
    except Exception as e:
        # If request fails (network error, timeout, etc.)
        return {
            "success": False,
            "customer_name": customer_name,
            "status_code": "Error",
            "response": str(e)
        }