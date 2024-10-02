from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from views import AuthView, TickerView, FundamentusView


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8080'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


app.include_router(AuthView.router, tags=['Authentication'])
app.include_router(TickerView.router, tags=['Specific Ticker'])
app.include_router(FundamentusView.router, tags=['Tickers'])
