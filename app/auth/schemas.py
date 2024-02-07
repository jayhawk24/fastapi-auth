from pydantic import BaseModel
from typing import Optional
from commons.enums import TokenKind


class RefreshTokenRequestSchema(BaseModel):
    refresh_token: str


class RefreshTokenResponseSchema(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str]
    token_kind: Optional[TokenKind]
