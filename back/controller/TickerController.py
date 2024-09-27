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
