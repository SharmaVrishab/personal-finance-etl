from abc import ABC, abstractmethod


class BaseExtractor(ABC):
    @abstractmethod
    def extract(self):
        """

        All extractors must implement this

        """
        pass
