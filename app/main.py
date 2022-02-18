from fastapi import FastAPI
from calculations import totalFees
from reqmodel import ReqModel

app = FastAPI()

@app.post("/delivery_fee/")
async def calcFee(req:ReqModel):
    
    fee = totalFees(req.number_of_items, req.delivery_distance,
    req.cart_value, req.time)
    
    return {"delivery_fee":fee}