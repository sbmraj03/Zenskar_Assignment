import csv
import io
import base64

def main(x: str):
    """
    Parse CSV file from base64 string.
    Returns list of customer rows.
    """
    
    # Convert base64 string back to file bytes
    try:
        file_bytes = base64.b64decode(x)
    except:
        # If decoding fails, return empty data
        return {"parsed_data": [], "total_rows": 0}
    
    # Try different text encodings to handle various CSV files
    for encoding in ['utf-8-sig', 'utf-8', 'latin-1']:
        try:
            file_content = file_bytes.decode(encoding)
            break  # Success! Use this encoding
        except:
            continue  # Try next encoding
    else:
        # If all encodings fail, use fallback
        file_content = file_bytes.decode('utf-8', errors='ignore')
    
    # Convert CSV text to list of dictionaries
    try:
        csv_reader = csv.DictReader(io.StringIO(file_content))
        rows = list(csv_reader)
        
        # Return data in expected format
        return {
            "parsed_data": rows,
            "total_rows": len(rows)
        }
    except:
        # If CSV parsing fails, return empty data
        return {"parsed_data": [], "total_rows": 0}