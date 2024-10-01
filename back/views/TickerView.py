from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from controller.TickerController import TickerController
from controller.AuthController import AuthController


router = APIRouter()
oauth2scheme = OAuth2PasswordBearer(tokenUrl='token')


@router.get('/ticker-info')
def ticker_info(ticker: str, token: str = Depends(oauth2scheme)):
    current_user = AuthController.get_current_user(token)
    asset = TickerController(ticker)
    if current_user is None:
        raise HTTPException(status_code=401, detail='Invalid token')
    return asset.asset_info()


@router.get('/ticket-calendar')
def ticket_calendar(ticker: str, token: str = Depends(oauth2scheme)):
    current_user = AuthController.get_current_user(token)
    asset = TickerController(ticker)
    if current_user is None:
        raise HTTPException(status_code=401, detail='Invalid token')
    return asset.asset_calendar()


@router.get('/ticket-news')
def ticket_news(ticker: str, token: str = Depends(oauth2scheme)):
    current_user = AuthController.get_current_user(token)
    asset = TickerController(ticker)
    if current_user is None:
        raise HTTPException(status_code=401, detail='Invalid token')
    return asset.asset_last_new()


@router.get('/ticket-holders')
def ticket_holders(ticker: str, token: str = Depends(oauth2scheme)):
    current_user = AuthController.get_current_user(token)
    asset = TickerController(ticker)
    if current_user is None:
        raise HTTPException(status_code=401, detail='Invalid token')
    return asset.asset_majors_holders()


@router.get('/ticker-data')
def ticker_data(ticker: str, token: str = Depends(oauth2scheme)):
    current_user = AuthController.get_current_user(token)
    if current_user is None:
        raise HTTPException(status_code=401, detail='Invalid token')
    asset = TickerController.get_asset_data(ticker)
    return asset
