# from typing import Union
from fastapi import FastAPI
from fastapi import Form
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import asyncio

from emailAutoGen import generateEmail

from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

class Data(BaseModel):
    yourname: str
    phone: str
    email: str
    customer: str
    product: str
    details: str
    result: str

# Configure CORS
origins = [
    "http://localhost:3000",  # Add your frontend origin(s) here
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can restrict this to specific HTTP methods (e.g., ["GET", "POST"])
    allow_headers=["*"],  # You can restrict this to specific headers if needed
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/submit", response_model=Data)
async def submit(data: Data):
    # Generate Email from Openai and LangChain 
    result = await generateEmail(data)
    await asyncio.sleep(3)

    # Data Processing
    data = await dataProcess(data, result)
    print(data)
    return data


async def dataProcess(data: Data, result: str):
    data = {
        "yourname": data.yourname,
        "phone": data.phone,
        "email": data.email,
        "customer": data.customer,
        "product": data.product,
        "details": data.details,
        "result": result
    }
    return data
