from pydantic import BaseModel, constr, EmailStr, ConfigDict


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    email: str
    is_active: bool


class SignUpRequestSchema(BaseModel):
    name: constr(min_length=3, max_length=50)
    email: EmailStr
    password: constr(min_length=8, max_length=50)


class SignUpResponseSchema(BaseModel):
    detail: str


class LoginRequestSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8, max_length=50)


class LoginResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
