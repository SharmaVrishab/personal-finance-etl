import pandas as pd


class Normalizer:
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        # Parse dates
        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"], errors="coerce")

        # Parse amounts
        if "amount" in df.columns:
            df["amount"] = (
                df["amount"]
                .astype(str)
                .str.replace(r"[\$,€£¥,\s]", "", regex=True)
                .str.replace(r"^\((.*)\)$", r"-\1", regex=True)
            )
            df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

        # Normalize description
        if "description" in df.columns:
            df["description"] = df["description"].fillna("").strip()

        # Normalize transaction type & category
        if "transaction_type" in df.columns:
            df["transaction_type"] = (
                df["transaction_type"].str.lower().fillna("unknown")
            )
        if "category" in df.columns:
            df["category"] = df["category"].str.lower().fillna("uncategorized")

        return df
