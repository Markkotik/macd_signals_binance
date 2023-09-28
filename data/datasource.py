from abc import ABC, abstractmethod
from typing import Any
from decouple import config


class DataSource(ABC):
    """
    Abstract class for data sources.
    """

    def __init__(self):
        self.symbol: str = config('SYMBOL')
        self.timeframe: str = config('TIMEFRAME')
        self.limit: int = config('LIMIT', default=300)

    @abstractmethod
    def get_data(self) -> Any:
        """
        Retrieve data based on the symbol, timeframe, and limit attributes.

        :return: DataFrame with the data.
        """
        pass

    @abstractmethod
    def connection_status(self) -> bool:
        """
        Check the connection status with the data source.

        :return: True if the connection is active, otherwise False.
        """
        pass

