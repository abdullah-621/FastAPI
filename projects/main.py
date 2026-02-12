from fastapi import FastAPI, Path, HTTPException,Query
import json

app = FastAPI()

def load_data():
  with open("patients.json", 'r') as f:
    data = json.load(f)
  return data

@app.get("/")
def hello(): 
  return {"massage":"Hello, I'm Abdullah Al Masum"}

@app.get("/about")
def about():
  return {"massage":"This is a project for doctor and patients"}

@app.get("/views")
def views():
  return load_data()


# path parameter
@app.get("/patient/{patient_id}")
def patient(patient_id : str = Path(..., description="ID of the patient", example="P001")):

  data = load_data()

  if patient_id in data:
    return data[patient_id]
  raise HTTPException(status_code=404, detail="Patient not found.")


# query parameter
@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height,weight or bmi"), order: str = Query('asc', description="Sort in asc ir desc order")):
  
  valid_fields = ['height', 'weight', 'bmi']

  if sort_by not in valid_fields:
    raise HTTPException(status_code=400, detail=f"Invalid field select form {valid_fields}")

  if order not in ['asc', 'desc']:
    raise HTTPException(status_code=400, detail="Invalide order setect between asc and desc")
  
  data= load_data()

  sort_order = True if order == "desc" else False

  sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse=sort_order)

  return sorted_data
  

