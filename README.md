A comprehensive ETL system for processing financial data from multiple sources (bank statements, credit cards, receipts) and generating insights.

## Features

- Extract data from CSV, JSON, and PDF sources
- Normalize and categorize transactions
- Detect and remove duplicates
- Generate spending analysis reports
- Memory-efficient streaming processing

## Project Structure

finance_etl/
├── src/ # Source code
├── data/ # Data files (ignored by git)
├── tests/ # Unit tests
├── config/ # Configuration files
└── requirements.txt

## Getting Started

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Add your financial data files to `data/input/`
4. Run the pipeline: `python -m src.pipeline`

## Technologies Used

- Python 3.8+
- Functional programming patterns
- Iterator-based processing
- Generator pipelines
