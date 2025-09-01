from .categorizer import Categorizer
from .deduplicator import Deduplicator
from .normalizer import Normalizer
from .validator import Validator


class TransactionTransformer:
    def __init__(self):
        self.steps = [
            Normalizer(),
            # Deduplicator(),
            Validator(),
            # Categorizer(),
        ]

    def transform(self, df):
        for step in self.steps:
            df = step.transform(df)
        return df


__all__ = ["TransactionTransformer"]
