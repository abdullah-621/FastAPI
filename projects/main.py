from fastapi import FastAPI, Path, HTTPException
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


@app.get("/patient/{patient_id}")
def patient(patient_id : str = Path(..., description="ID of the patient", example="P001")):

  data = load_data()

  if patient_id in data:
    return data[patient_id]
  raise HTTPException(status_code=404, detail="Patient not found.")