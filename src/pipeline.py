# Main orchestration


from extractor.csv_extractor import CSVExtractor


def run_pipeline():
    # step 1 - extract

    extractor = CSVExtractor()
    raw_data = extractor.extract_record(
        "/Users/vrishab/Documents/code/python/projects/personal-finance-etl/tests/test_transaction.csv"
    )

    print(raw_data)
    """
    ! finished
    """
    print("pipeline finished successfully")


if __name__ == "__main__":
    run_pipeline()
