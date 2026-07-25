from pydantic import BaseModel


class PredictionRequest(BaseModel):
    area: int
    bedrooms: int
    bathrooms: int
    mainroad: int
    basement: int
    stories: int
    guestroom: int
    hotwaterheating: int
    parking: int
    airconditioning: int
    furnishingstatus: int
    prefarea: int


class PredictionResponse(BaseModel):
    house_price: int
