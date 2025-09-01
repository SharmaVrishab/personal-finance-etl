import pandas as pd


class Validator:
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        required = ["date", "amount", "description"]
        # Ensure all required columns exist
        for col in required:
            if col not in df.columns:
                df[col] = pd.NA

        df["missing_fields"] = df[required].apply(
            lambda row: ",".join(
                col
                for col in required
                if pd.isna(row[col]) or str(row[col]).strip() == ""
            ),
            axis=1,
        )
        df["is_valid"] = df["missing_fields"].apply(lambda x: 1 if x == "" else 0)

        # Collect extra fields
        standard_fields = [
            "date",
            "amount",
            "description",
            "transaction_type",
            "category",
            "missing_fields",
            "is_valid",
        ]
        extra_fields = [col for col in df.columns if col not in standard_fields]

        if extra_fields:
            df["extra_fields"] = df[extra_fields].apply(
                lambda row: {k: v for k, v in row.items() if pd.notna(v)}, axis=1
            )

        return df
