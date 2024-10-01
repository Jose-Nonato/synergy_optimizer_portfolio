from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from controller.AuthController import AuthController
from controller.FundamentusController import FundamentusController


router = APIRouter()
oauth2scheme = OAuth2PasswordBearer(tokenUrl='token')


@router.get('/all-tickers')
def all_tickers(token: str = Depends(oauth2scheme)):
    current_user = AuthController.get_current_user(token)
    if current_user is None:
        raise HTTPException(status_code=401, detail='Invalid token')
    data = FundamentusController.get_all_papers()
    return data
