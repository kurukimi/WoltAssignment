from pydantic import BaseModel, PositiveInt

# Model to handle FastApi requests easily
class ReqModel(BaseModel):
    cart_value: PositiveInt
    delivery_distance: PositiveInt
    number_of_items: PositiveInt
    time: str