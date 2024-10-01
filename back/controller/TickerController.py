import yfinance as yf


class TickerController:
    def __init__(self, ticker):
        self.ticker = yf.Ticker(ticker)


    def asset_info(self):
        return self.ticker.info


    def asset_calendar(self):
        return self.ticker.calendar
    

    def asset_last_new(self):
        return self.ticker.news
    

    def asset_majors_holders(self):
        return self.ticker.major_holders


    @staticmethod
    def get_asset_data(ticker):
        print(ticker)
        data = yf.download(ticker, start='2015-01-01' , progress=False)
        return data.to_json()
