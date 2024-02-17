from pydantic import BaseModel

class MathRequest(BaseModel):
    numbers: str
    sign: str
    
class PasswordRequest(BaseModel):
    password: str
    
class DictionaryRequest(BaseModel):
    word: str