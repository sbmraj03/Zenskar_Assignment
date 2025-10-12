# Windmill Flow Scripts

This folder contains the Python scripts for the CSV customer import flow.

## Files

- `parse_csv_file.py` - Parses CSV files with encoding detection
- `transform_customer_data.py` - Transforms and validates customer data
- `sendtomockapi.py` - Sends data to MockAPI with error handling
- `generate_report.py` - Creates processing reports

## Usage

1. Import these scripts into your Windmill flow
2. Configure the MockAPI endpoint in `sendtomockapi.py`
3. Upload CSV files through the Windmill interface
4. Review processing reports

## Flow Order

1. Parse CSV File → 2. Transform Customer Data → 3. For Loop → 4. Send to MockAPI → 5. Generate Report