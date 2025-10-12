# Setup Guide

## Prerequisites

- Docker Desktop installed
- Windows/Mac/Linux

## Installation

### 1. Install Windmill

```bash
# Create project folder
mkdir csv-customer-import
cd csv-customer-import

# Download Windmill
curl -o docker-compose.yml https://raw.githubusercontent.com/windmill-labs/windmill/main/docker-compose.yml

# Start Windmill
docker compose up -d
```

### 2. Access Windmill

- Open browser: http://localhost:8000
- Create account and workspace

### 3. Create Flow

1. Click "+ Flow"
2. Name: `csv_customer_import`
3. Add Input: `csv_file` (String, Required)
4. Add steps from windmill/ folder

### 4. Configure MockAPI

1. Sign up at https://mockapi.io
2. Create project
3. Add "customers" resource
4. Update endpoint in `sendtomockapi.py`

## Test Setup

1. Upload `data/customers.csv`
2. Click "Run"
3. Check results

## Troubleshooting

- **Port 8000 busy**: Change port in docker-compose.yml
- **CSV encoding errors**: System handles multiple encodings automatically
- **API errors**: Check MockAPI configuration