# Main orchestration


from extractors.csv_extractor import CSVExtractor
from transformer import TransactionTransformer


def run_pipeline():
    # step 1 - extract

    extractor = CSVExtractor()
    raw_data = extractor.extract_record(
        "/Users/vrishab/Documents/code/python/projects/personal-finance-etl/tests/test_transaction.csv"
    )
    df = raw_data
    # step 2 - transformation
    transformer = TransactionTransformer()
    df = transformer.transform(df)
    print(df)
    print("pipeline finished successfully")


if __name__ == "__main__":
    run_pipeline()
