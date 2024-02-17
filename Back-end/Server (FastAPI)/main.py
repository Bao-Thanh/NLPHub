from model import DictionaryRequest
from model import PasswordRequest
from model import MathRequest

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from Module.Normal.math import calculator
from Module.Normal.password_strength import check_password_strength
from Module.Normal.dictionary import get_definitions_en2en

from Util.is_valid_number import is_valid_number

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/math")
async def math(request: MathRequest):
    nums = request.numbers.split()
    sign = request.sign
    
    if all(is_valid_number(num) for num in nums):
        return {"result": calculator(nums, sign)} 
    else:
        raise HTTPException(status_code=400, detail="Invalid request")   

@app.post("/check_password_strength/")
async def check_password_strength_api(request: PasswordRequest):
    result = check_password_strength(request.password)
    return {
                "password": result[0], 
                "strength": f"{result[1]:.2%}"
            }

@app.post("/dictionary")
async def define_word(request: DictionaryRequest):
    definitions = get_definitions_en2en(request.word)
    if not definitions:
        raise HTTPException(status_code=404, detail=f"No definition found for the word: {request.word}")
    return {"word": request.word, "definitions": definitions}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
