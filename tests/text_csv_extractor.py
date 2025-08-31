import os
import sys

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.extractor.csv_extractor import CSVExtractor

# Path to your test CSV - use the simpler approach
TEST_CSV = os.path.join(os.path.dirname(__file__), "test_transaction.csv")

# Alternative: If you want to be explicit about the full path
# TEST_CSV = "/Users/vrishab/Documents/code/python/projects/personal-finance-etl/tests/test_transaction.csv"

# 1️⃣ Initialize extractor
extractor = CSVExtractor()

# 2️⃣ Extract records
df = extractor.extract_record(TEST_CSV)

# 3️⃣ Print results
print("All rows:")
print(df)

print("\nValid rows:")
print(df[df["is_valid"] == 1])

print("\nInvalid rows:")
print(df[df["is_valid"] == 0])
