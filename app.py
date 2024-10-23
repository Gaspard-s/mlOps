from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load("regression.joblib")

app = FastAPI()


class HouseData(BaseModel):
    size: float
    nb_rooms: int
    garden: int

@app.post("/predict")
def predict(request: HouseData):
    input_array = np.array([[request.size, request.nb_rooms, request.garden]])
    prediction = model.predict(input_array)
    rounded_prediction = round(prediction[0], 2)
    return {"prediction": rounded_prediction}