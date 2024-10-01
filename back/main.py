from fastapi import FastAPI
from views import AuthView, TickerView, FundamentusView


app = FastAPI()


app.include_router(AuthView.router, tags=['Authentication'])
app.include_router(TickerView.router, tags=['Specific Ticker'])
app.include_router(FundamentusView.router, tags=['Tickers'])
