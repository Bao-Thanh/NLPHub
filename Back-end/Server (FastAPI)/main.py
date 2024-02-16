import json
from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from Module.Normal.math import calculator
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

class MathInput(BaseModel):
    numbers: str
    sign: str
    
@app.post("/math")
async def math(math_input: MathInput):
    nums = math_input.numbers.split()
    sign = math_input.sign
    
    if all(is_valid_number(num) for num in nums):
        return {"result": calculator(nums, sign)} 
    else:
        raise HTTPException(status_code=400, detail="Invalid request")   

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
