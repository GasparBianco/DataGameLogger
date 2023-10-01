from pydantic import BaseModel

class defaultResponse(BaseModel):
    detail: str

class AuthTokenResponse(BaseModel):
    access_token: str
    token_type: str