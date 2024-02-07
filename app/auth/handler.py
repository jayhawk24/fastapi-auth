from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from auth.tokens import verify_token, create_access_token
from db.database import get_db
from commons.enums import TokenKind
from auth.schemas import RefreshTokenResponseSchema, RefreshTokenRequestSchema
from auth.schemas import TokenData

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post("/refresh-token", response_model=RefreshTokenResponseSchema)
def refresh_token(payload: RefreshTokenRequestSchema, db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid Token")
    token_data: TokenData = verify_token(payload.refresh_token, credentials_exception)

    if token_data.token_kind != TokenKind.RefreshToken:
        raise credentials_exception

    access_token = create_access_token(data={"user_id": token_data.id})

    return RefreshTokenResponseSchema(access_token=access_token, token_type="bearer")
