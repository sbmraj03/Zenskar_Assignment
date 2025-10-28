## Demo Recording
Watch the demo here: https://drive.google.com/file/d/108tMJGMlH1z_NEuafcNdqBRRyP7c7GUG/view

# CSV Customer Import System - Zenskar Assignment

A Windmill-based system that processes CSV files and creates customers via MockAPI.

## Quick Start

1. **Setup Windmill**
   ```bash
   docker compose up -d
   # Access at http://localhost:8000
   ```

2. **Configure MockAPI**
   - Update `PROJECT_ID` in `sendtomockapi.py`
   - Use your MockAPI endpoint

3. **Upload CSV**
   - Use Windmill interface
   - Upload CSV with customer data
   - Get processing report

## Project Structure

```
├── windmill/           # Windmill flow scripts
├── data/              # Sample CSV files
├── docs/              # Documentation
└── screenshots/       # Demo images
```

## Features

- ✅ CSV parsing with encoding detection
- ✅ Data validation and transformation
- ✅ API integration with error handling
- ✅ Row-level error reporting
- ✅ Processing summary reports

## Documentation

- [Setup Guide](docs/SETUP.md) - Installation instructions
- [User Guide](docs/USER_GUIDE.md) - How to use the system
- [Developer Guide](docs/DEVELOPER_GUIDE.md) - How to modify transformations

## Sample Data

Includes `customers.csv` with 10 sample records for testing.

## Technology Stack

- **Platform**: Windmill
- **Language**: Python 3.11
- **API**: MockAPI.io
- Windmill (Local Docker Instance)

---

*Built for Zenskar Implementation Engineer Intern assignment*
