from fastapi import FastAPI, Path, HTTPException,Query, Body
import json
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional

# todo ->>>>> pydantic model

class Patient(BaseModel):

  id : Annotated[str, Field(..., description="ID of the patient", examples=["P001"])]
  name : Annotated[str,Field(..., description="Name of the patient", examples=["Abdullah"])]
  city : Annotated[str, Field(..., description="City of the patient", examples=["Dhaka"])]
  age : Annotated[int, Field(..., gt = 0, lt=120, description="Age of the patients")]
  gender : Annotated[Literal["Male", "Female", "Others"], Field(..., description="Gender of the patients")]
  height : Annotated[float, Field(...,gt=0, description="Height of the patients(mts)")]
  weight : Annotated[float, Field(...,gt=0, description="Weight of the patients (kg)")]

  @computed_field
  @property
  def bmi(self) -> float:
    BMI = round(self.weight / (self.height**2),2)
    return BMI
  
  @computed_field
  @property
  def verdict(self) -> str:
    if self.bmi < 18.5:
      return "Underweight"
    elif 18.5 <= self.bmi < 24.9:
      return "Healthy"
    elif 25 <= self.bmi < 30:
      return "Overweight"
    else:
      return "Obesity"
    


class PatientUpdate(BaseModel):

  name: Annotated[Optional[str], Field(default=None)]
  city: Annotated[Optional[str], Field(default=None)]
  age: Annotated[Optional[int], Field(default=None, gt=0, lt=120)]
  gender: Annotated[Optional[Literal["Male", "Female", "Others"]], Field(default=None)]
  height: Annotated[Optional[float], Field(default=None, gt=0)]
  weight: Annotated[Optional[float], Field(default=None, gt=0)]

# todo ->>>>> pydantic model


# todo ->>>>>>>>>>>>>>>>>>>>>>>>-<<<<<<<<<<<<<<<<<<<<<<<<<<<<-
app = FastAPI()

def load_data():
  with open("patients.json", 'r') as f:
    data = json.load(f)
  return data

def save_data(data):
  with open("patients.json", 'w') as f:
    json.dump(data, f)
# todo ->>>>>>>>>>>>>>>>>>>>>>>>-<<<<<<<<<<<<<<<<<<<<<<<<<<<<<-

# todo ->>>>>>>> READ part (get) <<<<<<<<<-

@app.get("/")
def hello(): 
  return {"message":"Hello, I'm Abdullah Al Masum"}

@app.get("/about")
def about():
  return {"message":"This is a project for doctor and patients"}

@app.get("/views")
def views():
  return load_data()


# path parameter
@app.get("/patient/{patient_id}")
def get_patient(patient_id : str = Path(..., description="ID of the patient", examples=["P001"])):

  data = load_data()

  if patient_id in data:
    return data[patient_id]
  raise HTTPException(status_code=404, detail="Patient not found.")


# query parameter
@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height,weight or bmi"), order: str = Query('asc', description="Sort in asc ir desc order")):
  
  valid_fields = ['height', 'weight']

  if sort_by not in valid_fields:
    raise HTTPException(status_code=400, detail=f"Invalid field select form {valid_fields}")

  if order not in ['asc', 'desc']:
    raise HTTPException(status_code=400, detail="Invalide order setect between asc and desc")
  
  data= load_data()

  sort_order = True if order == "desc" else False

  sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse=sort_order)

  return sorted_data
  
# todo ->>>>>>>>>>>>>> READ part <<<<<<<<<<<<<<<-


# todo ->>>>>>>>>>> CREAT part (post) <<<<<<<<<<<<<<-
# creat Patient
@app.post("/create")
def creat_patient(patient : Patient):

  # load existing data
  data = load_data()

  # chech the patient is already exists
  if patient.id in data:
    raise HTTPException(status_code=400, detail="Patient Already into database")
  
  # new patient add to the database
  data[patient.id] = patient.model_dump(exclude = ['id'])
  
  save_data(data)

  return JSONResponse(status_code=201, content={'message' : 'Patient created successfully'})

# todo ->>>>>>>>>>>>> CREAT part <<<<<<<<<<<<<<<-

# todo ->>>>>>>>>>>>>> Update part <<<<<<<<<<<<<<-

@app.put("/edit/{patient_id}")
def update_patient(patient_id: str , patient_update : PatientUpdate):
  data = load_data()

  if patient_id not in data:
    raise HTTPException(status_code=404, detail="patient not found")
  
  existing_patient_info = data[patient_id]

  updated_patient_info = patient_update.model_dump(exclude_unset=True)  # JSON to Dict

  for key, value in updated_patient_info.items():
    existing_patient_info[key] = value
  
  #existing_patient_info -> pydantic object -> updated bmi + verdict
  existing_patient_info['id'] = patient_id
  patient_pydantic_obj = Patient(**existing_patient_info)

  #-> pydantic object -> dict
  existing_patient_info = patient_pydantic_obj.model_dump(exclude='id')

  # add this dict into database
  data[patient_id] = existing_patient_info

  # save data
  save_data(data)


  return JSONResponse(status_code=200, content={"message" : 'patient update successfully'})
  
# todo ->>>>>>>>>>>>>> Update part <<<<<<<<<<<<<<-

