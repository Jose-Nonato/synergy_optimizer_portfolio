from fastapi import FastAPI
from views import AuthView, TickerView


app = FastAPI()


app.include_router(AuthView.router, tags=['Authentication'])
app.include_router(TickerView.router, tags=['Ticker'])
