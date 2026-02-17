# 'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad','guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea'

import pickle
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Annotated,Literal
import pandas as pd

with open('model.pkl', 'rb') as f:
  model = pickle.load(f)

class HouseInfo(BaseModel):
  area : Annotated[float, Field(..., gt=0, description="Area of the house")]
  bedrooms : Annotated[int, Field(..., gt=0, description="bedrooms of the house")]
  bathrooms : Annotated[int, Field(..., gt=0, description="bathrooms of the house")]
  stories : Annotated[int, Field(..., gt=0, description="stories of the house")]
  mainroad : Annotated[Literal[0,1], Field(..., description="mainroad of the house")]
  guestroom : Annotated[Literal[0,1], Field(..., description="guestroom of the house")]
  basement : Annotated[Literal[0,1], Field(..., description="basement of the house")]
  hotwaterheating : Annotated[Literal[0,1], Field(..., description="hotwaterheating of the house")]
  airconditioning : Annotated[Literal[0,1], Field(..., description="airconditioning of the house")]
  parking : Annotated[int, Field(...,ge=0, description="parking of the house")]
  prefarea : Annotated[Literal[0,1], Field(..., description="prefarea of the house")]


app = FastAPI()

@app.get("/hello")
def hello():
  return "This is House price prediction model"

@app.post("/predict")
def predict_price(data: HouseInfo):
  user_input = {
    "area" : data.area,
    "bedrooms" : data.bedrooms,
    "bathrooms" : data.bathrooms,
    "stories" : data.stories,
    "mainroad" : data.mainroad,
    "guestroom" : data.guestroom,
    "basement" : data.basement,
    "hotwaterheating" : data.hotwaterheating,
    "airconditioning" : data.airconditioning,
    "parking" : data.parking,
    "prefarea" : data.prefarea
  }

  user_input = pd.DataFrame([user_input])

  prediction = model.predict(user_input)[0]

  return JSONResponse(status_code=200, content={"House price : " : round(float(prediction),2)})
  # return {"House price": round(float(prediction), 2)}

