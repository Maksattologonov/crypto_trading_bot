import pandas as pd


class Aggregate:
    ts = ''
    price = ''
    url = ''

    def aggregate_data(self, period: str):
        # read our csv file
        data = pd.read_csv(self.url)
        # read timestamp
        data[self.ts] = pd.to_datetime(data[self.ts])
        # indexing read csv
        data.set_index(self.ts, inplace=True)
        # return sample  with period
        return data[self.price].resample(period).mean()

    def aggregate_olhc(self, open: str, close: str):
        # read our csv file
        data = pd.read_csv(self.url)
        # read timestamp
        data[self.ts] = pd.to_datetime(data[self.ts])
        # indexing read csv
        data.set_index(self.ts, inplace=True)
        # show period open and close arguments
        ohlc_open = data[self.price].resample(open).ohlc()
        ohlc_close = data[self.price].resample(close).ohlc()
        return ohlc_open, ohlc_close

    def calculate_ema(self, length):
        # read our csv file
        data = pd.read_csv(self.url)
        # average move calculate
        alpha = 2 / (length + 1)
        ema_values = []
        ema_prev = None
        # take every price column
        for price in data['PRICE']:
            if ema_prev is None:
                ema = price
            else:
                # simple math, calculate ema
                ema = alpha * price + (1 - alpha) * ema_prev
            ema_values.append(ema)
            ema_prev = ema

        data['EMA'] = ema_values

        return data


agg = Aggregate()
agg.ts = 'TS'
agg.price = 'PRICE'
agg.url = 'prices.csv'
data = agg.aggregate_data('5min')
data_ol = agg.aggregate_olhc('5min', '1H')
data_ema = agg.calculate_ema(14)
print('aggregated', data)
print('olhc', data_ol)
print('ema', data_ema)
""" I use the Object programming bcz its easy to read and readable and simple"""
