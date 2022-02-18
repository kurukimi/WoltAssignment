from pydantic import BaseModel

class Constants(BaseModel):
    # Cart value
    minCartValue: int
    freeOfChargeValue: int
    # Distance
    minDistance: int
    minDistanceFee: int
    additionalDistance: int
    additionalDistanceFee: int
    # Items
    maxItems: int
    additionalItemFee: int
    # Other
    rushTimeMultiplier: float
    maxDeliveryPrice: int



const = Constants(
    minCartValue=1000,
    minDistance=1000,
    minDistanceFee=200,
    additionalDistance=500,
    additionalDistanceFee = 100,
    maxItems=4,
    additionalItemFee=50,
    freeOfChargeValue=10000,
    rushTimeMultiplier=1.1,
    maxDeliveryPrice=1500
    )