import pytest

from meta.data_processor import DataProcessor
from meta.data_processors._base import DataSource


def test_alphavantage():
    TRADE_START_DATE = "2020-09-01"
    TRADE_END_DATE = "2021-09-11"

    TIME_INTERVAL = "1d"
    TECHNICAL_INDICATOR = [
        "macd",
        "boll_ub",
        "boll_lb",
        "rsi_30",
        "dx_30",
        "close_30_sma",
        "close_60_sma",
    ]
    kwargs = {}
    p = DataProcessor(
        data_source=DataSource.alphavantage,
        start_date=TRADE_START_DATE,
        end_date=TRADE_END_DATE,
        time_interval=TIME_INTERVAL,
        **kwargs,
    )

    ticker_list = ["IBM"]

    p.download_data(ticker_list=ticker_list)

    p.clean_data()
    p.add_turbulence()
    p.add_technical_indicator(TECHNICAL_INDICATOR)
    # p.add_vix()

    price_array, tech_array, turbulence_array = p.run(
        ticker_list, TECHNICAL_INDICATOR, if_vix=False, cache=True
    )
    assert price_array.shape[0] == tech_array.shape[0]
    assert turbulence_array is None
