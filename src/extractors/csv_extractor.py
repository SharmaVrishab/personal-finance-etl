import os

import pandas as pd

from .base_extractor import BaseExtractor


class CSVExtractor(BaseExtractor):
    def __init__(self, encoding: str = "utf-8"):
        self.encoding = encoding

    def extract(self, file_path: str) -> pd.DataFrame:
        """Read and clean CSV data."""
        if not os.path.exists(file_path):
            raise ValueError(f"Source not found: {file_path}")

        df = pd.read_csv(file_path, encoding=self.encoding)

        # Normalize column names
        df.columns = [c.strip().lower() for c in df.columns]

        # Replace empty/whitespace-only strings with NaN
        df.replace(r"^\s*$", pd.NA, regex=True, inplace=True)

        # Drop rows where all values are NaN
        df = df.dropna(how="all")

        return df

    # Optional: keep extract_record as alias for backwards compatibility
    def extract_record(self, source_path: str) -> pd.DataFrame:
        return self.extract(source_path)

    # def extract_record(self, source_path: str) -> pd.DataFrame:
    #     """
    #     Extract and normalize CSV data using pandas.

    #     Steps:
    #     1️⃣ Load CSV
    #     2️⃣ Standardize column names
    #     3️⃣ Clean empty/whitespace fields
    #     4️⃣ Parse dates
    #     5️⃣ Parse amounts
    #     6️⃣ Normalize descriptions
    #     7️⃣ Normalize transaction type & category
    #     8️⃣ Check required fields and mark valid/invalid
    #     9️⃣ Collect extra fields
    #     """
    #     print(source_path)
    #     # STEP 1: Defensive check - file existence
    #     if not os.path.exists(source_path):
    #         raise ValueError(f"Source not found: {source_path}")

    #     # STEP 1: Load CSV
    #     df = pd.read_csv(source_path, encoding=self.encoding)

    #     # STEP 2: Standardize column names
    #     field_mapping = {
    #         "transaction_date": "date",
    #         "Date": "date",
    #         "amount_usd": "amount",
    #         "Amount": "amount",
    #         "merchant": "description",
    #         "Merchant": "description",
    #         "type": "transaction_type",
    #         "category": "category",
    #     }
    #     df = df.rename(columns={col: field_mapping.get(col, col) for col in df.columns})
    #     df.columns = [c.strip().lower() for c in df.columns]  # normalize headers

    #     # STEP 3: Replace empty strings or whitespace-only with NA
    #     df.replace(r"^\s*$", pd.NA, regex=True, inplace=True)

    #     # STEP 4: Parse dates
    #     if "date" in df.columns:
    #         df["date"] = pd.to_datetime(  # type ignore
    #             df["date"], errors="coerce", infer_datetime_format=True
    #         )  # type: ignore

    #     # STEP 5: Parse amounts
    #     if "amount" in df.columns:
    #         df["amount"] = (
    #             df["amount"]
    #             .astype(str)
    #             .str.replace(r"[\$,€£¥,\s]", "", regex=True)
    #             .str.replace(r"^\((.*)\)$", r"-\1", regex=True)  # handle (123) → -123
    #         )
    #         df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    #     # STEP 6: Normalize descriptions
    #     if "description" in df.columns:
    #         df["description"] = df["description"].fillna("").str.strip()

    #     # STEP 7: Normalize transaction_type & category
    #     if "transaction_type" in df.columns:
    #         df["transaction_type"] = (
    #             df["transaction_type"].str.lower().fillna("unknown")
    #         )
    #     if "category" in df.columns:
    #         df["category"] = df["category"].str.lower().fillna("uncategorized")

    #     # STEP 8: Check required fields and mark valid/invalid
    #     required = ["date", "amount", "description"]
    #     df["missing_fields"] = df[required].apply(
    #         lambda row: ",".join(
    #             [
    #                 col
    #                 for col in required
    #                 if pd.isna(row[col])
    #                 or (isinstance(row[col], str) and row[col].strip() == "")
    #             ]
    #         ),
    #         axis=1,
    #     )
    #     df["is_valid"] = df["missing_fields"].apply(lambda x: 1 if x == "" else 0)

    #     # STEP 9: Collect extra fields not in standard schema
    #     standard_fields = [
    #         "date",
    #         "amount",
    #         "description",
    #         "transaction_type",
    #         "category",
    #         "missing_fields",
    #         "is_valid",
    #     ]
    #     extra_fields = [col for col in df.columns if col not in standard_fields]

    #     if extra_fields:
    #         df["extra_fields"] = df[extra_fields].apply(
    #             lambda row: {k: v for k, v in row.items() if pd.notna(v)}, axis=1
    #         )

    #     return df
